<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <?php
    $num1 = 30;
    $num2 = 6;
    $soma = $num1 + $num2;
    $sub = $num1 - $num2;
    $mult = $num1 * $num2;
    $div = $num1 / $num2;
    echo"A soma de $num1 e $num2 é $soma <br>";
    echo "A subtração de $num1 e $num2 é $sub <br>";
    echo "A multiplicação de $num1 e $num2 é $mult <br>";
    echo "A divisão de $num1 e $num2 é $div <br>";

    if ($div > 10) {
        echo "O resultado da divisão é maior que 10";
    } elseif ($div == 10) {
        echo "O resultado da divisão é igual a 10";
    } else {
        echo "O resultado da divisão é menor que 10";
    }
    ?>
    
</body>
</html>