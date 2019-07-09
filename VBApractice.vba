Public Sub practice()
    Dim i As Integer
     i = 1
     Do While i <= 10

        If ActiveCell.Value > 10 Then
            ActiveCell.Interior.Color = RBG(255, 0, 0)
        End If

        ActiveCell.Offset(1, 0).Select


        i = i + 1

    Loop
End Sub

================================================================================

Public Sub UserSortInput()
    Dim userInput As String
    Dim promptmsg As String
    Dim tryAgain As Integer


    promptmsg = "Enter a numeric result to sort..." & vbCrLf & _
        "1 --- Sort by Division" & vbCrLf & _
        "2 --- Sort by Category" & vbCrLf & _
        "3 --- Sort by Total"
    userInput = InputBox("What is your fav color?")

    If userInput = "1" Then
        DivisionSort
    ElseIf userInput = "2" Then
        CategorySort
    ElseIf userInput = "3" Then
        TotalSort
    Else
       tryAgain = MsgBox("Invalid Value! Try again?", vbYesNo)
       If tryAgain = 6 Then
            UserSortInput
    End If


End Sub

===============================================================================

Public Sub CleanUpData()
    Dim i As Integer

    i = 1

    Do While i <= Worksheets.Count
        Worksheets(i).Select

    AddHeaders
    ColorHeader

    i = i + 1

    Loop

End Sub


================================================================================

Public Sub Automate()
    Dim lastCell As String
    Dim i As Integer

    i = 1

    Do While i <= Worksheets.Count
        Worksheets(i).Select


    Range("F2").Select

    Selection.End(xlDown).Select

    lastCell = ActiveCell.Address(False, False)

    ActiveCell.Offset(1, 0).Select
    ActiveCell.Value = "=SUM(F2:" & lastCell & ")"

    i = i + 1

End Sub
===============================================================================
