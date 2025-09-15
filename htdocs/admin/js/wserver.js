function WSBus(opts) {
    this.baseUrl = opts.baseUrl;
    this.path = opts.path || '/ws/staff-events';
    this.tokenUrl = opts.tokenUrl;
    this.onopen = opts.onopen || function () {
    };
    this.onclose = opts.onclose || function () {
    };
    this.onerror = opts.onerror || function () {
    };
    this.backoffMin = opts.backoffMin || 1000;
    this.backoffMax = opts.backoffMax || 10000;
    this.ws = null;
    this.stopped = false;
    this.backoff = this.backoffMin;
    this.handlers = new Map();
}

WSBus.prototype._dispatch = function (evt, payload, raw) {
    var list = this.handlers.get(evt);
    if (list) for (var i = 0; i < list.length; i++) try {
        list[i](payload, raw);
    } catch (e) {
    }
    var any = this.handlers.get('*');
    if (any) for (var j = 0; j < any.length; j++) try {
        any[j](evt, payload, raw);
    } catch (e) {
    }
};
WSBus.prototype.on = function (evt, cb) {
    if (!this.handlers.has(evt)) this.handlers.set(evt, []);
    this.handlers.get(evt).push(cb);
    return this;
};
WSBus.prototype.off = function (evt, cb) {
    var list = this.handlers.get(evt);
    if (!list) return this;
    this.handlers.set(evt, list.filter(function (f) {
        return f !== cb;
    }));
    return this;
};
WSBus.prototype.once = function (evt, cb) {
    var self = this;

    function wrap(a, b, c) {
        self.off(evt, wrap);
        cb(a, b, c);
    }

    return this.on(evt, wrap);
};
WSBus.prototype._fetchToken = function () {
    return $.getJSON(this.tokenUrl).then(function (d) {
        return d.token;
    });
};
WSBus.prototype._connect = function () {
    var self = this;
    this._fetchToken().done(function (token) {
        var url = self.baseUrl + self.path + '?token=' + encodeURIComponent(token);
        self.ws = new WebSocket(url);
        self.ws.onopen = function () {
            self.backoff = self.backoffMin;
            self.onopen(self.ws, url);
        };
        self.ws.onmessage = function (e) {
            var txt = e.data, evt = 'message', payload = txt;
            try {
                var obj = JSON.parse(txt);
                var key = obj.event || obj.type || obj.evt;
                if (key) {
                    evt = String(key);
                    payload = ('payload' in obj) ? obj.payload : obj.data;
                }
            } catch (_) {
            }
            self._dispatch(evt, payload, txt);
        };
        self.ws.onclose = function (ev) {
            self.onclose(ev);
            if (self.stopped) return;
            setTimeout(function () {
                self._connect();
            }, self.backoff);
            self.backoff = Math.min(self.backoff * 2, self.backoffMax);
        };
        self.ws.onerror = function (err) {
            self.onerror(err);
            try {
                self.ws.close();
            } catch (_) {
            }
        };
    }).fail(function () {
        if (self.stopped) return;
        setTimeout(function () {
            self._connect();
        }, Math.min(self.backoff * 2, self.backoffMax));
    });
};
WSBus.prototype.start = function () {
    this.stopped = false;
    this._connect();
    return this;
};
WSBus.prototype.stop = function () {
    this.stopped = true;
    if (this.ws) try {
        this.ws.close();
    } catch (_) {
    }
    return this;
};