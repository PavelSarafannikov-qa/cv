/* Это объявление переменной, мы наши кнопку по тегу */
const button = document.getElementById("credo");

/* Тут на кнопку навешиваем обрабочик, который ждёт клика и тогда запустит логику */
button.addEventListener('click', function() {
	alert('Старайся, Павлик! 🥴')
})