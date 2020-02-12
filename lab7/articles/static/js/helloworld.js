var groupmates = [
    {
        "name": "Александр",
        "surname": "Иванов",
        "group": "БВТ1702",
        "marks": [4, 3, 5]
    },
    {
        "name": "Иван",
        "surname": "Петров",
        "group": "БСТ1702",
        "marks": [4, 4, 4]
    },
    {
        "name": "Кирилл",
        "surname": "Смирнов",
        "group": "БАП1801",
        "marks": [5, 5, 5]
    }
];
// Добавляет digit пробелов в конец таблицы
var rpad = function(str, digit) 
{
    digit = digit - str.length;
    for (var i = 1; i <= digit; i++)
    {
        str = str + " "; 
    }
    return str;
};

// Выводит в виде таблицы список студентов
var printStudents = function(students){ 
    console.log(
        rpad("Имя", 15),
        rpad("Фамилия", 15),
        rpad("Группа", 8),
        rpad("Оценки", 20)
    );

    for (var i = 0; i<=students.length-1; i++){
        console.log(
            rpad(students[i]["name"], 15),
            rpad(students[i]["surname"], 15),
            rpad(students[i]["group"], 8),
            rpad(students[i]["marks"], 20)
        );
    }
    console.log('\n');
};

// Фильтрация
var filter_by_group = function(students,filter_group){
    for (var i = 0; i <= students.length-1; i ++)
    {
        if (students[i]["group"] == filter_group) 
        {
            console.log(
            rpad(students[i]["name"], 15),
            rpad(students[i]["surname"], 15),
            rpad(students[i]["group"], 8),
            rpad(students[i]["marks"], 20)
        );
        } 
    }
    console.log('\n');
}

var mid_number = function(array) {
    var sum = 0;
    for (var i = 0; i <= array.length-1; i++){
        sum = sum + array[i];
    }
    answer = sum / array.length;
    return answer;
}

var filter_by_mid = function(students,mid){
    for (var i = 0; i <= students.length-1; i ++)
    {
        if (mid_number(students[i]["marks"]) >= mid) 
        {
            console.log(
            rpad(students[i]["name"], 15),
            rpad(students[i]["surname"], 15),
            rpad(students[i]["group"], 8),
            rpad(students[i]["marks"], 20)
        );
        } 
    }
    console.log('\n');
}

printStudents(groupmates);
console.log("Отфильтрованый список по группе: \n")

filter_by_group(groupmates, "БСТ1702")
console.log("Отфильтрованый список по средней оценке: \n")

filter_by_mid(groupmates,4.3)