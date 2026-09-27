import urllib.request
import json
import xml.etree.ElementTree as ET
from typing import Dict, Any, Optional

class ReleaseResolver:
    """Zero-Token GitHub Release Resolver using Atom Feeds & API fallback"""
    
    @staticmethod
    def get_atom_feed_url(repo: str) -> str:
        return f"https://github.com/{repo.strip('/')}/releases.atom"

    @classmethod
    def resolve_latest_via_atom(cls, repo: str, timeout: int = 10) -> Optional[Dict[str, Any]]:
        url = cls.get_atom_feed_url(repo)
        req = urllib.request.Request(url, headers={"User-Agent": "tool-omni-updater/0.1.0"})
        try:
            with urllib.request.urlopen(req, timeout=timeout) as resp:
                xml_data = resp.read()
                root = ET.fromstring(xml_data)
                ns = {"atom": "http://www.w3.org/2005/Atom"}
                entry = root.find("atom:entry", ns)
                if entry is None:
                    return None
                
                title = entry.find("atom:title", ns)
                updated = entry.find("atom:updated", ns)
                link = entry.find("atom:link", ns)
                
                tag = title.text if title is not None else ""
                return {
                    "repo": repo,
                    "latest_tag": tag,
                    "updated_at": updated.text if updated is not None else "",
                    "release_url": link.attrib.get("href") if link is not None else "",
                    "source": "ATOM_FEED"
                }
        except Exception as e:
            return None
