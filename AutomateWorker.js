let elements2;
let texts2 = [];

// Функция для обновления массива текстов
function updateTexts() {
    elements2 = document.querySelectorAll('.markdown.prose.w-full.break-words');
    texts2 = []; // Очищаем массив перед заполнением
    elements2.forEach((element) => {
        texts2.push(element.innerText); // Добавляем новые элементы
    });
}

// Функция для паузы
function sleep(ms) {
    return new Promise(resolve => setTimeout(resolve, ms));
}

// Функция для сохранения последнего элемента массива в файл
async function saveLastArrayElementToFile(waitTime) {
    updateTexts(); // Обновляем массив текстов
    let lastText = texts2[texts2.length - 1]; // Обновляем последний элемент
    await sleep(waitTime); // Добавляем задержку перед скачиванием
    const blob = new Blob([lastText], { type: "text/plain" });
    const link = document.createElement("a");
    link.href = URL.createObjectURL(blob);
    link.download = "dataOutput.txt"; // Имя файла для последнего элемента
    link.click();
}

let lastSvgElement = null; // Переменная для хранения предыдущего элемента
let downloadCount = 0; // Переменная для подсчета вызовов

function checkElementChanges() {
    const svgElement = document.querySelector('svg.icon-2xl');

    if (svgElement && lastSvgElement !== svgElement) {
        lastSvgElement = svgElement; // Обновляем ссылку на элемент сразу, чтобы избежать повторений
        downloadCount++; // Увеличиваем счетчик вызовов
        let waitTime = 10000 + (downloadCount * 1000); // Основное ожидание + 1 секунда за каждый вызов
        setTimeout(() => {
            console.log('Кнопка изменилась!');
            // Запуск сохранения последнего элемента массива с добавленным временем ожидания
            saveLastArrayElementToFile(waitTime);
        }, waitTime);
    } else if (!svgElement) {
        console.log('Элемент не найден, продолжаю искать...');
        lastSvgElement = null; // Обновляем ссылку на элемент
    }

    setTimeout(checkElementChanges, 1000);
}

// Запускаем проверку
checkElementChanges();