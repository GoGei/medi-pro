from core.Utils.redis import BaseRedis


class ExtractAllergyCauseRedis(BaseRedis):
    KEY = 'medicine:tasks:sync:extract_allergy_cause'
    TTL = 30


class ExtractAllergyTypesRedis(BaseRedis):
    KEY = 'medicine:tasks:sync:extract_allergy_types'
    TTL = 30


class ExtractAllergyReactionRedis(BaseRedis):
    KEY = 'medicine:tasks:sync:extract_allergy_reaction'
    TTL = 30


class LoadIcd10Redis(BaseRedis):
    KEY = 'medicine:tasks:sync:load_icd10'
    TTL = 60 * 5  # 5 min
