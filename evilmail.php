<?php
$from      = 'auto@instagram.com';
$titulo    = 'Password';
$mensaje   = 'Buenos dias, nos ponemos en contacto con usted porracion de nuestras bases de datos, puede que su password haya sido comprometida. Por favor cambie la passwor desde el siguiente link. Gracias';
$cabeceras = 'From: jhojanson18@gmail.com' . "
" .
    'Reply-To: nice@eo-ripper.py' . "
" .
    'X-Mailer: PHP/' . phpversion();

mail($from, $titulo, $mensaje, $cabeceras);
echo "Todo OK!";
?>