Attribute VB_Name = "Ä£¿é1"

Dim cmax As Long
Dim rmax As Long

Sub AddRows()
    Dim r As Integer
    Dim c As Integer
    r = 3
    c = 5
    Cells(c, r).Select
    
    If Cells(c, r).Text <> "" And Range("C2:C4").MergeCells = True Then
        Selection.EntireColumn.Insert , CopyOrigin:=xlFormatFromLeftOrAbove
        Selection.EntireColumn.Insert , CopyOrigin:=xlFormatFromLeftOrAbove
        Selection.EntireColumn.Insert , CopyOrigin:=xlFormatFromLeftOrAbove
    Else
        MsgBox ("Warning! Changes in this sheet may have been done.")
        ChoiceOfYNC = MsgBox("New colums anyway?", vbYesNoCancel, "Confirm Warning:")
        If ChoiceOfYNC = vbYes Then
            Selection.EntireColumn.Insert , CopyOrigin:=xlFormatFromLeftOrAbove
            Selection.EntireColumn.Insert , CopyOrigin:=xlFormatFromLeftOrAbove
            Selection.EntireColumn.Insert , CopyOrigin:=xlFormatFromLeftOrAbove
        ElseIf ChoiceOfYNC = vbNo Then
            MsgBox ("Skip this step.")
        ElseIf ChoiceOfYNC = vbCancel Then
            MsgBox ("Aborted.")
            End
        Else
            MsgBox ("Error!")
            End
        End If
        
    End If
End Sub
Sub FormRange()
    Dim r As Integer
    Dim c As Integer
    r = 3
    c = 5
    Do
        r = r + 1
        'Cells(c, r).Select
    Loop Until Cells(c, r).Borders(xlEdgeLeft).LineStyle = xlNone
    r = r - 2
    'Cells(c, r).Select
    Do
        c = c + 1
        'Cells(c, r).Select
        
    Loop Until Cells(c, r).Interior.Color <> 16777215
    c = c - 1
    Cells(c, r).Select
    cmax = c
    rmax = r
End Sub

Sub MainAct()
    Dim r2 As Long
    Dim c As Integer
    Dim r As Integer
    AddRows
    FormRange
    r = 3
    c = 5
    Cells(c, r).Select
    Dim ContentInC As String
    Dim ContentInD As String
    Dim ContentInE As String
    Dim rmax2 As Long
    Dim cmax2 As Long
    
    For c = c To cmax
        cmax2 = cmax
        rmax2 = rmax
        ContentInC = "=sum(H" & Trim(Str(c)) & ":V" & Trim(Str(c)) & ")"
        ContentInD = "=sum(H" & Trim(Str(c)) & ":" & ConvertToLetter(rmax2) & Trim(Str(c)) & ")"
        r = 9
        ContentInE = "="
        
        Do
            r2 = r
            ContentInE = ContentInE & ConvertToLetter(r2) & Trim(Str(c))
            r = r + 3
            If r > rmax Then
                Exit Do
            Else
                ContentInE = ContentInE & "+"
                
            End If
        Loop
        
        Cells(c, 3).Formula = ContentInC
        
        Cells(c, 4).Formula = ContentInD
        
        Cells(c, 5).Formula = ContentInE
        
    Next c

End Sub

Function ConvertToLetter(iCol As Long) As String
   Dim a As Long
   Dim b As Long
   a = iCol
   ConvertToLetter = ""
   Do While iCol > 0
      a = Int((iCol - 1) / 26)
      b = (iCol - 1) Mod 26
      ConvertToLetter = Chr(b + 65) & ConvertToLetter
      iCol = a
   Loop
End Function


