const goBack = () => {
  if (confirm("登録画面に戻りますか？")) {
    return true;
  }
  return false;
};

const copy = () => {
  const textarea = document.createElement("textarea");
  const result = document.getElementById("result").innerText;

  textarea.value = result;
  document.body.appendChild(textarea);
  textarea.select();
  document.execCommand("copy");
  document.body.removeChild(textarea);
  alert("結果をクリップボードにコピーしました！");
};

const closeModal = (parent) => {
  parent.innerHTML = "";
  showNotification = false;
  sessionStorage.setItem("modalClosed", false);
};

let modalClosed = sessionStorage.getItem("modalClosed");
if (modalClosed) {
  const regexp = /help.*/;
  if (!regexp.test(location.href.split("/").at(-1))) {
    closeModal(document.getElementById("notification"));
  }
}
