document.addEventListener('DOMContentLoaded', () => {
  const taskForm = document.getElementById('task-form');
  const taskInput = document.getElementById('task-input');
  const taskList = document.getElementById('task-list');

  function saveTasks(tasks) {
    localStorage.setItem('tasks', JSON.stringify(tasks));
  }

  function loadTasks() {
    const tasks = JSON.parse(localStorage.getItem('tasks') || '[]');
    return tasks;
  }

  function render(tasks) {
    taskList.innerHTML = '';
    tasks.forEach((t) => {
      const li = document.createElement('li');
      li.textContent = t;
      taskList.appendChild(li);
    });
  }

  taskForm.addEventListener('submit', (e) => {
    e.preventDefault();
    const value = taskInput.value.trim();
    if (!value) return;
    const tasks = loadTasks();
    tasks.push(value);
    saveTasks(tasks);
    render(tasks);
    taskInput.value = '';
  });

  render(loadTasks());
});
