from dataclasses import dataclass


@dataclass
class CVersionData:
	sSub: str
	iReleaseVersion: int


@dataclass
class CRequestVersionData:
	sSub: str