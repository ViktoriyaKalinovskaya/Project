Код для простой и примитивной игры "Змейка". 
Для её написания использовались набор модулей Pygame и отдельно модуль Random.
Вначале создавались основные положения необходимые для создания поля, на котором будет происходить действие: окно, начальное тело змейки и еда.
Включая их рандомное появление на поле с использованием модуля random (randrange). После программа стала дополняться функционалом в виде увеличения длинны тела змейки при
"съедании" условного фрукта или грызуна; задержке движения змейки при запуске игры с помощью функции .tick(); привязка клавишей для управления движением змейки и запрет на
"прохождение" через саму себя, т.е. если змейка ползет вправо, она не сможет поврнуться влево и проползти по себе. Также с помощью условного оператора if установленно
ограничение на передвижение за пределы так называемого поля, а с применением цикла while True и проверкой правильного окончания программы через цикл for, на экран выводиться 
надпись "GAME OVER", как и надпись с ведением счета "Score: ", созданная с помощью метода render().
