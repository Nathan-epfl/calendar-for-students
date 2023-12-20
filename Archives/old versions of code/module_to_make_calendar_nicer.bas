Attribute VB_Name = "Module2"
Option Explicit
Sub nice_everything()
    Dim day, hour, tempshift, iter_end_group As Integer
    hour = 0
    tempshift = 0
    Dim temp As String
    Dim ini_address As String

    
    Application.DisplayAlerts = False
    Dim Dynamic_array As Variant
    ReDim Dynamic_array(0)
    
    Range("B2").Activate
    Range("B2").Select
    ini_address = ActiveCell.Address
    
    
    Dim arr_of_subj As Variant
    ReDim arr_of_subj(0)
    Dim column As Integer
    Dim row As Integer
    For column = 0 To 6
        For row = 0 To 31
            If IsInArray(ActiveCell.Offset(row, column), arr_of_subj) = False Then
                arr_of_subj(UBound(arr_of_subj)) = ActiveCell.Offset(row, column)
                ReDim Preserve arr_of_subj(0 To UBound(arr_of_subj) + 1)
            End If
        Next
    Next
    
    
    
    
    For day = 0 To 6
        Do While hour < 31
            Do While ActiveCell.Offset(hour, 0).Value = ActiveCell.Offset(hour + tempshift, 0).Value And hour + tempshift < 32
                tempshift = tempshift + 1
            Loop
                Dynamic_array(UBound(Dynamic_array)) = hour + tempshift - 1
                ReDim Preserve Dynamic_array(0 To UBound(Dynamic_array) + 1)
                hour = hour + tempshift
                tempshift = 0
        Loop
        hour = -1
        For iter_end_group = 0 To UBound(Dynamic_array) - 1
            temp = ActiveCell.Value
            Range(ActiveCell, ActiveCell.Offset(Dynamic_array(iter_end_group) - hour - 1, 0)).Merge
            ActiveCell.Select
            If (ActiveCell.Value <> "") And (ActiveCell.Value <> " ") Then
                With Selection
                    .HorizontalAlignment = xlCenter
                    .VerticalAlignment = xlCenter
                End With
                With Selection.Borders(xlEdgeLeft)
                    .LineStyle = xlContinuous
                    .ColorIndex = 0
                  .TintAndShade = 0
                 .Weight = xlMedium
                End With
                With Selection.Borders(xlEdgeTop)
                    .LineStyle = xlContinuous
                    .ColorIndex = 0
                    .TintAndShade = 0
                    .Weight = xlMedium
                End With
                With Selection.Borders(xlEdgeBottom)
                    .LineStyle = xlContinuous
                    .ColorIndex = 0
                    .TintAndShade = 0
                    .Weight = xlMedium
                End With
                With Selection.Borders(xlEdgeRight)
                    .LineStyle = xlContinuous
                    .ColorIndex = 0
                    .TintAndShade = 0
                    .Weight = xlMedium
                End With
                With Selection.Interior
                    .Pattern = xlSolid
                    .PatternColorIndex = xlAutomatic
                    .ThemeColor = xlThemeColorDark1
                    .TintAndShade = subj_to_color(arr_of_subj, temp)
                    .PatternTintAndShade = 0
                End With
            Else
                With Selection
                    .HorizontalAlignment = xlCenter
                    .VerticalAlignment = xlCenter
                End With
                With Selection.Borders(xlEdgeLeft)
                    .LineStyle = xlContinuous
                    .ColorIndex = 0
                  .TintAndShade = 0
                 .Weight = xlMedium
                End With
                With Selection.Borders(xlEdgeTop)
                    .LineStyle = xlContinuous
                    .ColorIndex = 0
                    .TintAndShade = 0
                    .Weight = xlMedium
                End With
                With Selection.Borders(xlEdgeBottom)
                    .LineStyle = xlContinuous
                    .ColorIndex = 0
                    .TintAndShade = 0
                    .Weight = xlMedium
                End With
                With Selection.Borders(xlEdgeRight)
                    .LineStyle = xlContinuous
                    .ColorIndex = 0
                    .TintAndShade = 0
                    .Weight = xlMedium
                End With
                With Selection.Interior
                    .Pattern = xlSolid
                    .PatternColorIndex = xlAutomatic
                    .ThemeColor = xlThemeColorDark1
                    .TintAndShade = 0
                    .PatternTintAndShade = 0
                End With
            End If
            hour = Dynamic_array(iter_end_group)
            ActiveCell.Offset(1, 0).Activate
        Next
        ReDim Dynamic_array(0)
        Range(ini_address).Activate
        ActiveCell.Offset(0, day + 1).Activate
        hour = 0
        iter_end_group = 0

    Next
    Range("A2").Activate
    Range("A2").Select
    ActiveCell.FormulaR1C1 = "8:00"
    Range("A3").Select
    ActiveCell.FormulaR1C1 = ""
    Range("A2:A3").Select
    Selection.AutoFill Destination:=Range("A2:A33"), Type:=xlFillDefault
    
    
    Range("I2").Activate
    ActiveCell.FormulaR1C1 = "8:00"
    Range("I2").Select
    Selection.Font.Bold = True
    Selection.Borders(xlDiagonalDown).LineStyle = xlNone
    Selection.Borders(xlDiagonalUp).LineStyle = xlNone
    With Selection.Borders(xlEdgeLeft)
        .LineStyle = xlContinuous
        .ColorIndex = 0
        .TintAndShade = 0
        .Weight = xlThin
    End With
    With Selection.Borders(xlEdgeTop)
        .LineStyle = xlContinuous
        .ColorIndex = 0
        .TintAndShade = 0
        .Weight = xlThin
    End With
    With Selection.Borders(xlEdgeBottom)
        .LineStyle = xlContinuous
        .ColorIndex = 0
        .TintAndShade = 0
        .Weight = xlThin
    End With
    With Selection.Borders(xlEdgeRight)
        .LineStyle = xlContinuous
        .ColorIndex = 0
        .TintAndShade = 0
        .Weight = xlThin
    End With
    With Selection.Borders(xlInsideVertical)
        .LineStyle = xlContinuous
        .ColorIndex = 0
        .TintAndShade = 0
        .Weight = xlThin
    End With
    With Selection.Borders(xlInsideHorizontal)
        .LineStyle = xlContinuous
        .ColorIndex = 0
        .TintAndShade = 0
        .Weight = xlThin
    End With
    Range("I3").Select
    Range("I3").Activate
    Selection.Borders(xlDiagonalDown).LineStyle = xlNone
    Selection.Borders(xlDiagonalUp).LineStyle = xlNone
    With Selection.Borders(xlEdgeLeft)
        .LineStyle = xlContinuous
        .ColorIndex = 0
        .TintAndShade = 0
        .Weight = xlThin
    End With
    With Selection.Borders(xlEdgeTop)
        .LineStyle = xlContinuous
        .ColorIndex = 0
        .TintAndShade = 0
        .Weight = xlThin
    End With
    With Selection.Borders(xlEdgeBottom)
        .LineStyle = xlContinuous
        .ColorIndex = 0
        .TintAndShade = 0
        .Weight = xlThin
    End With
    With Selection.Borders(xlEdgeRight)
        .LineStyle = xlContinuous
        .ColorIndex = 0
        .TintAndShade = 0
        .Weight = xlThin
    End With
    With Selection.Borders(xlInsideVertical)
        .LineStyle = xlContinuous
        .ColorIndex = 0
        .TintAndShade = 0
        .Weight = xlThin
    End With
    With Selection.Borders(xlInsideHorizontal)
        .LineStyle = xlContinuous
        .ColorIndex = 0
        .TintAndShade = 0
        .Weight = xlThin
    End With
    ActiveCell.FormulaR1C1 = ""
    Range("I2:I3").Select
    Selection.AutoFill Destination:=Range("I2:I33"), Type:=xlFillDefault
    
    With Range("I2:I3").Borders(xlEdgeLeft)
        .LineStyle = xlContinuous
        .ColorIndex = 0
        .TintAndShade = 0
        .Weight = xlMedium
    End With
    Range(Range(ini_address).Offset(-1, -1), Range(ini_address).Offset(31, 7)).Select
    Selection.Columns.AutoFit
End Sub

Function subj_to_color(arr_of_subj As Variant, subj As String) As Double
    Dim iter_num, num_of_subj As Integer
    num_of_subj = UBound(arr_of_subj)
    For iter_num = 0 To num_of_subj
        If arr_of_subj(iter_num) = subj Then
        subj_to_color = -0.4 * iter_num / num_of_subj - 0.1
        End If
    Next
End Function


Sub take_subj()
Dim arr_of_subj As Variant
ReDim arr_of_subj(0)
Dim column As Integer
Dim row As Integer
For column = 0 To 6
    For row = 0 To 31
        If IsInArray(ActiveCell.Offset(row, column), arr_of_subj) = False Then
            arr_of_subj(UBound(arr_of_subj)) = ActiveCell.Offset(row, column)
            ReDim Preserve arr_of_subj(0 To UBound(arr_of_subj) + 1)
        End If
    Next
Next
End Sub


Public Function IsInArray(stringToBeFound As String, arr As Variant) As Boolean
    Dim i
    For i = LBound(arr) To UBound(arr)
        If arr(i) = stringToBeFound Then
            IsInArray = True
            Exit Function
        End If
    Next i
    IsInArray = False

End Function


