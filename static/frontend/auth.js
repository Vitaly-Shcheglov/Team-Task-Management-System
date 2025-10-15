export function login(email, password) {
  return new Promise((resolve) => {
    setTimeout(() => {
      resolve({ success: true, user: { email } });
    }, 300);
  });
}
