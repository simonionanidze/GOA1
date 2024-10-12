document.addEventListener('DOMContentLoaded', () => {
    const taskInput = document.getElementById('taskInput');
    const addTaskBtn = document.getElementById('addTaskBtn');
    const taskList = document.getElementById('taskList');
    const clearTasksBtn = document.getElementById('clearTasksBtn');

    // Load tasks from localStorage
    loadTasks();

    // Add task event listener
    addTaskBtn.addEventListener('click', () => {
        const taskText = taskInput.value.trim();
        if (taskText) {
            addTask(taskText);
            taskInput.value = '';
        }
    });

    // Clear all tasks event listener
    clearTasksBtn.addEventListener('click', clearAllTasks);

    // Function to add a task
    const addTask = (taskText) => {
        const li = document.createElement('li');
        li.innerHTML = `
            <input type="checkbox" class="taskCheckbox">
            <span>${taskText}</span>
            <button class="deleteBtn">Delete</button>
        `;

        // Event listener for checkbox
        li.querySelector('.taskCheckbox').addEventListener('change', (e) => {
            li.querySelector('span').classList.toggle('completed', e.target.checked);
            saveTasks();
        });

        // Event listener for delete button
        li.querySelector('.deleteBtn').addEventListener('click', () => {
            li.remove();
            saveTasks();
        });

        taskList.appendChild(li);
        saveTasks();
    };

    // Function to clear all tasks
    const clearAllTasks = () => {
        taskList.innerHTML = '';
        localStorage.removeItem('tasks');
    };

    // Function to save tasks to localStorage
    const saveTasks = () => {
        const tasks = [];
        taskList.querySelectorAll('li').forEach(li => {
            const taskText = li.querySelector('span').textContent;
            const completed = li.querySelector('.taskCheckbox').checked;
            tasks.push({ text: taskText, completed });
        });
        localStorage.setItem('tasks', JSON.stringify(tasks));
    };

    // Function to load tasks from localStorage
    const loadTasks = () => {
        const tasks = JSON.parse(localStorage.getItem('tasks')) || [];
        tasks.forEach(task => {
            addTask(task.text);
            if (task.completed) {
                const lastTaskLi = taskList.lastElementChild;
                lastTaskLi.querySelector('.taskCheckbox').checked = true;
                lastTaskLi.querySelector('span').classList.add('completed');
            }
        });
    };
});
