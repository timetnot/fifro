document.addEventListener("DOMContentLoaded", function () {
  const registerModal = new bootstrap.Modal(document.getElementById("registerModal"));
  const loginModal = new bootstrap.Modal(document.getElementById("loginModal"));
  const codeModal = new bootstrap.Modal(document.getElementById("codeModal"));

  const registerForm = document.getElementById("registerForm");
  const loginForm = document.getElementById("loginForm");
  const codeForm = document.getElementById("codeForm");

  const passwordInput = document.getElementById("registerPassword");
  const passwordConfirmInput = document.getElementById("registerPasswordConfirm");
  const passwordMismatchError = document.getElementById("passwordMismatchError");

  const codeError = document.getElementById("codeError");

  let generatedCode = null;

  function checkPasswordsMatch() {
    if (passwordInput.value !== passwordConfirmInput.value) {
      passwordMismatchError.classList.remove("d-none");
      return false;
    } else {
      passwordMismatchError.classList.add("d-none");
      return true;
    }
  }

  passwordInput.addEventListener("input", checkPasswordsMatch);
  passwordConfirmInput.addEventListener("input", checkPasswordsMatch);

  registerForm.addEventListener("submit", function (e) {
    e.preventDefault();

    if (!registerForm.checkValidity()) {
      registerForm.classList.add("was-validated");
      return;
    }

    if (!checkPasswordsMatch()) {
      return;
    }

    generatedCode = Math.floor(100000 + Math.random() * 900000).toString();
    console.log("Код подтверждения:", generatedCode);

    registerModal.hide();
    codeModal.show();
  });

  loginForm.addEventListener("submit", function (e) {
    e.preventDefault();

    if (!loginForm.checkValidity()) {
      loginForm.classList.add("was-validated");
      return;
    }

    alert("Успешный вход");
    loginModal.hide();
  });

  codeForm.addEventListener("submit", function (e) {
    e.preventDefault();

    const userCode = document.getElementById("confirmationCode").value.trim();

    if (userCode === generatedCode) {
      codeError.classList.add("d-none");
      alert("Регистрация подтверждена! Можно войти.");
      codeModal.hide();
      loginModal.show();
    } else {
      codeError.classList.remove("d-none");
    }
  });

  document.getElementById("codeModal").addEventListener("show.bs.modal", function () {
    codeError.classList.add("d-none");
    document.getElementById("confirmationCode").value = "";
  });

  document.getElementById("registerModal").addEventListener("show.bs.modal", () => {
    registerForm.classList.remove("was-validated");
    passwordMismatchError.classList.add("d-none");
    registerForm.reset();
  });

  document.getElementById("loginModal").addEventListener("show.bs.modal", () => {
    loginForm.classList.remove("was-validated");
    loginForm.reset();
  });
});
