import re

class SemVer:
    """Semantic Version Parser and Comparator"""
    @staticmethod
    def parse(version_str: str) -> tuple:
        clean = re.sub(r'^[vV]', '', str(version_str).strip())
        parts = []
        for x in clean.split('.'):
            num = re.findall(r'^\d+', x)
            if num:
                parts.append(int(num[0]))
            else:
                parts.append(0)
        while len(parts) < 3:
            parts.append(0)
        return tuple(parts[:3])

    @classmethod
    def compare(cls, v1: str, v2: str) -> int:
        """Returns 1 if v1 > v2, -1 if v1 < v2, 0 if equal"""
        p1 = cls.parse(v1)
        p2 = cls.parse(v2)
        if p1 > p2: return 1
        if p1 < p2: return -1
        return 0

    @classmethod
    def is_newer(cls, candidate_version: str, current_version: str) -> bool:
        return cls.compare(candidate_version, current_version) > 0
