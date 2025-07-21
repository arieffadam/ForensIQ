rule SuspiciousExe
{
    meta:
        description = "Detects suspicious EXE files"
        author = "ForensIQ MVP"
        version = "1.0"
    strings:
        $a = "This program cannot be run in DOS mode"
    condition:
        $a
}

rule ExampleMalware
{
    meta:
        description = "Detects Example Malware"
        author = "ForensIQ MVP"
        version = "1.0"
    strings:
        $b = "malicious_string"
    condition:
        $b
}