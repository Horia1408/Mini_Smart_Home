 <?php

        $pathFile = "/var/fpwork/hcostina/proiect/trunk/control.txt";
        $File = fopen($pathFile, 'w') or die("Unable to open file!");
        fwrite($File, $_GET["temper"]);
        fclose($File);

 ?>

<html>
<title>Control</title>
<body>
<p>Temperatura trimisa</p>
<p>
<form method="get" action="/index.php">
	<button type="submit">Inapoi</button>
</form>
</p>
</body>
</html>
