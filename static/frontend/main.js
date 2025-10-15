document.addEventListener('DOMContentLoaded', () => {
  const authSection = document.getElementById('auth-section');
  const tasksSection = document.getElementById('tasks-section');
  const authForm = document.getElementById('auth-form');
  const authError = document.getElementById('auth-error');
  const logoutBtn = document.getElementById('logout-btn');

  const auth = {
    set(user) {
      localStorage.setItem('user', JSON.stringify(user));
    },
    get() {
      const u = localStorage.getItem('user');
      return u ? JSON.parse(u) : null;
    },
    clear() {
      localStorage.removeItem('user');
    }
  };

  function showSection(section) {
    if (section === 'auth') {
      authSection.hidden = false;
      tasksSection.hidden = true;
    } else {
      authSection.hidden = true;
      tasksSection.hidden = false;
    }
  }

  const currentUser = auth.get();
  if (currentUser) {
    showSection('tasks');
  } else {
    showSection('auth');
  }

  authForm.addEventListener('submit', (e) => {
    e.preventDefault();
    const email = document.getElementById('email').value.trim();
    const password = document.getElementById('password').value;

    if (email && password) {
      auth.set({ email });
      authError.textContent = '';
      showSection('tasks');
      // Инициализируем задачи после входа
      loadTasksFromStorage();
    } else {
      authError.textContent = 'Пожалуйста, введите корректные данные.';
    }
  });

  logoutBtn.addEventListener('click', () => {
    auth.clear();
    localStorage.removeItem('tasks');
    document.getElementById('task-list').innerHTML = '';
    document.getElementById('task-input').value = '';
    showSection('auth');
  });

  if (currentUser) {
    loadTasksFromStorage();
  }
});

function loadTasksFromStorage() {
  const tasks = JSON.parse(localStorage.getItem('tasks') || '[]');
  renderTasks(tasks);
}
function renderTasks(tasks) {
  const list = document.getElementById('task-list');
  if (!list) return;
  list.innerHTML = '';
  tasks.forEach((t, idx) => {
    const li = document.createElement('li');
    li.textContent = t;
    list.appendChild(li);
  });
}
