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
