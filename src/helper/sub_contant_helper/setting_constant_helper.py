SERVICE_NAME = "nectorsdk"

API_BASE_URL = "https://platform.nector.io"

API_BASE_HEADER = {
    "accept": "application/json",
    "content-type": "application/json",
    "x-source": "web"
}

API_MAP = {
    "coupon": {
        "create": {"endpoint": "/coupons", "prefix": "/api/v2/merchant", "has_authorization": True, "has_signature": True},
        "get": {"endpoint": "/coupons/{id}", "prefix": "/api/v2/merchant", "has_authorization": True},
        "save": {"endpoint": "/coupons/{id}", "prefix": "/api/v2/merchant", "has_authorization": True, "has_signature": True},
        "list": {"endpoint": "/coupons", "prefix": "/api/v2/merchant", "has_authorization": True}
    },
    "currency": {
        "get": {"endpoint": "/currencies/{id}", "prefix": "/api/v2/merchant", "has_authorization": True},
        "list": {"endpoint": "/currencies", "prefix": "/api/v2/merchant", "has_authorization": True}
    },
    "deal": {
        "reward": {"endpoint": "/dealrewards", "prefix": "/api/v2/merchant", "has_authorization": True, "has_signature": True},
        "get": {"endpoint": "/deals/{id}", "prefix": "/api/v2/merchant", "has_authorization": True},
        "list": {"endpoint": "/deals", "prefix": "/api/v2/merchant", "has_authorization": True}
    },
    "lead": {
        "create": {"endpoint": "/leads", "prefix": "/api/v2/merchant", "has_authorization": True, "has_signature": True},
        "get": {"endpoint": "/leads/{id}", "prefix": "/api/v2/merchant", "has_authorization": True},
        "save": {"endpoint": "/leads/{id}", "prefix": "/api/v2/merchant", "has_authorization": True, "has_signature": True},
        "list": {"endpoint": "/leads", "prefix": "/api/v2/merchant", "has_authorization": True}
    },
    "notification": {
        "get": {"endpoint": "/notifications/{id}", "prefix": "/api/v2/merchant", "has_authorization": True},
        "list": {"endpoint": "/notifications", "prefix": "/api/v2/merchant", "has_authorization": True}
    },
    "review": {
        "create": {"endpoint": "/reviews", "prefix": "/api/v2/merchant", "has_authorization": True, "has_signature": True},
        "get": {"endpoint": "/reviews/{id}", "prefix": "/api/v2/merchant", "has_authorization": True},
        "save": {"endpoint": "/reviews/{id}", "prefix": "/api/v2/merchant", "has_authorization": True, "has_signature": True},
        "delete": {"endpoint": "/reviews/{id}", "prefix": "/api/v2/merchant", "has_authorization": True},
        "list": {"endpoint": "/reviews", "prefix": "/api/v2/merchant", "has_authorization": True}
    },
    "setting": {
        "get": {"endpoint": "/settings/{id}", "prefix": "/api/v2/merchant", "has_authorization": True}
    },
    "swap": {
        "create": {"endpoint": "/swaps", "prefix": "/api/v2/merchant", "has_authorization": True, "has_signature": True},
        "get": {"endpoint": "/swaps/{id}", "prefix": "/api/v2/merchant", "has_authorization": True},
        "list": {"endpoint": "/swaps", "prefix": "/api/v2/merchant", "has_authorization": True}
    },
    "task": {
        "get": {"endpoint": "/tasks/{id}", "prefix": "/api/v2/merchant", "has_authorization": True},
        "list": {"endpoint": "/tasks", "prefix": "/api/v2/merchant", "has_authorization": True}
    },
    "taskactivity": {
        "create": {"endpoint": "/taskactivities", "prefix": "/api/v2/merchant", "has_authorization": True, "has_signature": True},
        "get": {"endpoint": "/taskactivities/{id}", "prefix": "/api/v2/merchant", "has_authorization": True},
        "list": {"endpoint": "/taskactivities", "prefix": "/api/v2/merchant", "has_authorization": True}
    },
    "wallet": {
        "create": {"endpoint": "/wallets", "prefix": "/api/v2/merchant", "has_authorization": True, "has_signature": True},
        "get": {"endpoint": "/wallets/{id}", "prefix": "/api/v2/merchant", "has_authorization": True},
        "save": {"endpoint": "/wallets/{id}", "prefix": "/api/v2/merchant", "has_authorization": True, "has_signature": True},
        "list": {"endpoint": "/wallets", "prefix": "/api/v2/merchant", "has_authorization": True}
    },
    "wallettransaction": {
        "create": {"endpoint": "/wallettransactions", "prefix": "/api/v2/merchant", "has_authorization": True, "has_signature": True},
        "get": {"endpoint": "/wallettransactions/{id}", "prefix": "/api/v2/merchant", "has_authorization": True},
        "save": {"endpoint": "/wallettransactions/{id}", "prefix": "/api/v2/merchant", "has_authorization": True, "has_signature": True},
        "list": {"endpoint": "/wallettransactions", "prefix": "/api/v2/merchant", "has_authorization": True}
    }
}
