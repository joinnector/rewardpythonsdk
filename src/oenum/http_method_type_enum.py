from enum import Enum

class HttpMethodType(Enum):
	GET = "get"
	POST = "post"
	PUT = "put"
	DELETE = "delete"
	HEAD = "head"
	OPTIONS = "options"