{
    "apis": {
        "children": {},
        "parents": {
            "/users": {
                "RESTName": "user",
                "relationship": "root",
                "operations": [
                    {
                        "availability": null,
                        "method": "GET"
                    },
                    {
                        "availability": null,
                        "method": "POST"
                    }
                ],
                "resourceName": "users"
            },
            "/tasks/id/users": {
                "RESTName": "task",
                "relationship": "member",
                "resourceName": "tasks",
                "operations": [
                    {
                        "availability": null,
                        "method": "GET"
                    },
                    {
                        "availability": null,
                        "method": "PUT"
                    }
                ]
            }
        },
        "self": {
            "/users/{id}": {
                "RESTName": "user",
                "entityName": "User",
                "operations": [
                    {
                        "availability": null,
                        "method": "PUT"
                    },
                    {
                        "availability": null,
                        "method": "DELETE"
                    },
                    {
                        "availability": null,
                        "method": "GET"
                    }
                ],
                "resourceName": "users"
            }
        }
    },
    "model": {
        "RESTName": "user",
        "attributes": {
            "firstName": {
                "allowedChars": null,
                "allowedChoices": null,
                "autogenerated": false,
                "availability": null,
                "channel": null,
                "creationOnly": false,
                "defaultOrder": false,
                "defaultValue": null,
                "description": "The first name",
                "exposed": true,
                "filterable": true,
                "format": null,
                "maxLength": 1024,
                "maxValue": null,
                "minLength": 1,
                "minValue": null,
                "orderable": true,
                "readOnly": false,
                "required": true,
                "transient": false,
                "type": "string",
                "unique": false
            },
            "lastName": {
                "allowedChars": null,
                "allowedChoices": null,
                "autogenerated": false,
                "availability": null,
                "channel": null,
                "creationOnly": false,
                "defaultOrder": false,
                "defaultValue": null,
                "description": "The last name",
                "exposed": true,
                "filterable": true,
                "format": null,
                "maxLength": 1024,
                "maxValue": null,
                "minLength": 1,
                "minValue": null,
                "orderable": true,
                "readOnly": false,
                "required": true,
                "transient": false,
                "type": "string",
                "unique": false
            },
            "userName": {
                "allowedChars": null,
                "allowedChoices": null,
                "autogenerated": false,
                "availability": null,
                "channel": null,
                "creationOnly": false,
                "defaultOrder": false,
                "defaultValue": null,
                "description": "the login",
                "exposed": true,
                "filterable": true,
                "format": null,
                "maxLength": 1024,
                "maxValue": null,
                "minLength": 1,
                "minValue": null,
                "orderable": true,
                "readOnly": false,
                "required": true,
                "transient": false,
                "type": "string",
                "unique": true
            }
        },
        "description": "Represent a user",
        "entityName": "User",
        "extends": [],
        "package": "todo-list",
        "resourceName": "users"
    }
}
