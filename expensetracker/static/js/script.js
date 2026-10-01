function Display(){
    var taskname = document.getElementById("taskname").value;
    console.log(taskname);
    var element = document.createElement("div");
    element.innerHTML = `<label>${taskname}</label> <button onclick="DeleteTask(event)">Delete</button>`;

    var taskcontainer = document.getElementById("tasklist")
    taskcontainer.appendChild(element);
}

function DeleteTask(event){
    event.target.parentElement.remove();
}