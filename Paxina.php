<?php
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    $start_level = intval($_POST['start_level']);
    $end_level = intval($_POST['end_level']);
    
    // Chamada ao script Python
    $command = escapeshellcmd("python3 script.py $start_level $end_level");
    $output = shell_exec($command);
    echo "<h2>Resultados:</h2>";
    echo nl2br($output); // Imprime o resultado do script Python
}
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Calculadora de Experiencia</title>
</head>
<body>
    <h1>Calculadora de Experiencia</h1>
    <form method="POST" action="">
        <label for="start_level">Nivel inicial:</label>
        <input type="number" id="start_level" name="start_level" required>
        <br>
        <label for="end_level">Nivel final:</label>
        <input type="number" id="end_level" name="end_level" required>
        <br>
        <button type="submit">Calcular</button>
    </form>
</body>
</html>