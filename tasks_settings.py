{
    "version": "2.0.0",
    "tasks": [
        {
            "label": "l",
            "type": "shell",
            "command": "python",
            "args": [
                "${workspaceFolder}\\compile_shell.py",
                "${relativeFile}",
                "${lineNumber}",
                "-pl"
            ],
            "group": {
                "kind": "build",
                "isDefault": true
            },
            "problemMatcher": []
        },
        {
            "label": "best",
            "type": "shell",
            "command": "python",
            "args": [
                "${workspaceFolder}\\compile_shell.py",
                "${relativeFile}",
                "${lineNumber}",
                "-p"
            ],
            "group": {
                "kind": "build",
                "isDefault": true
            },
            "problemMatcher": []
        },
        {
            "label": "m",
            "type": "shell",
            "command": "python",
            "args": [
                "${workspaceFolder}\\compile_shell.py",
                "${relativeFile}",
                "${lineNumber}",
                "-pm"
            ],
            "group": {
                "kind": "build",
                "isDefault": true
            },
            "problemMatcher": []
        },
        {
            "label": "s",
            "type": "shell",
            "command": "python",
            "args": [
                "${workspaceFolder}\\compile_shell.py",
                "${relativeFile}",
                "${lineNumber}",
                "-s"
            ],
            "group": {
                "kind": "build",
                "isDefault": true
            },
            "problemMatcher": []
        },
        {
            "label": "i",
            "type": "shell",
            "command": "python",
            "args": [
                "${workspaceFolder}\\compile_shell.py",
                "${relativeFile}",
                "${lineNumber}",
                "-il"
            ],
            "group": {
                "kind": "build",
                "isDefault": true
            },
            "problemMatcher": []
        },
    ]
}