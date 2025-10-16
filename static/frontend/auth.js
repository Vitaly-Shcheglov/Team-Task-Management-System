export function login(email, password) {
  return new Promise((resolve, reject) => {
    fetch('/api/users/login/', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ email, password }),
    })
    .then(response => {
      if (!response.ok) {
        throw new Error('Ошибка при входе');
      }
      return response.json();
    })
    .then(data => {
      resolve({ success: true, user: data.user });
    })
    .catch(error => {
      reject(error);
    });
  });
}

(function() {
  const loginForm = document.getElementById('login-form');
  const registerForm = document.getElementById('register-form');
  const loginLink = document.getElementById('show-register-link');
  const registerLink = document.getElementById('show-login-link');
  const authTitle = document.getElementById('auth-title');
  const statusEl = document.getElementById('auth-status');

  function showLogin() {
    loginForm.style.display = '';
    registerForm.style.display = 'none';
    authTitle.textContent = 'Вход';
    statusEl.textContent = '';
  }

  function showRegister() {
    loginForm.style.display = 'none';
    registerForm.style.display = '';
    authTitle.textContent = 'Регистрация';
    statusEl.textContent = '';
  }

  loginLink?.addEventListener('click', function(e) {
    e.preventDefault();
    showRegister();
  });

  registerLink?.addEventListener('click', function(e) {
    e.preventDefault();
    showLogin();
  });

  registerForm?.addEventListener('submit', async function(e) {
    e.preventDefault();
    const name = document.getElementById('reg-name').value.trim();
    const email = document.getElementById('reg-email').value.trim();
    const password = document.getElementById('reg-password').value;
    const password2 = document.getElementById('reg-password-repeat').value;

    if (!name || !email || !password || !password2) {
      statusEl.textContent = 'Пожалуйста, заполните все поля.';
      return;
    }
    if (password.length < 8) {
      statusEl.textContent = 'Пароль должен содержать не менее 8 символов.';
      return;
    }
    if (password !== password2) {
      statusEl.textContent = 'Пароли не совпадают.';
      return;
    }

    try {
      const res = await fetch('/api/users/register/', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ name, email, password, password2 })
      });
      if (res.status === 201) {
        statusEl.textContent = 'Регистрация успешна. Можно войти в систему.';
        showLogin();
      } else {
        const data = await res.json().catch(() => ({}));
        const msg = data?.message || 'Не удалось зарегистрироваться. Попробуйте позже.';
        statusEl.textContent = msg;
      }
    } catch (err) {
      statusEl.textContent = 'Ошибка сети. Попробуйте позже.';
    }
  });

  loginForm?.addEventListener('submit', async function(e) {
    e.preventDefault();
    const email = document.getElementById('login-email').value.trim();
    const password = document.getElementById('login-password').value;

    if (!email || !password) {
      statusEl.textContent = 'Пожалуйста, введите email и пароль.';
      return;
    }

    try {
      const res = await login(email, password);
      if (res.success) {statusEl.textContent = 'Успешный вход!';
      }
    } catch (error) {
      statusEl.textContent = 'Неверные учетные данные.';
    }
  });

  showLogin();
})();
