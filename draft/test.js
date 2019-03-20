function createGuid() {
      return (((1 + Math.random()) * 0x10000) | 0).toString(16).substring(1);
}
function ref() {
     var guid = createGuid() + createGuid() + "-" + createGuid() + "-" + createGuid() + createGuid() + "-" + createGuid() + createGuid() + createGuid(); //CreateGuid();
     $("#txthidGuid").val(guid);
     $("#divYzmImg").html("<img alt='点击刷新验证码！' name='validateCode' id='ImgYzm' onclick='ref()'  title='点击切换验证码' src='/ValiCode/CreateCode/?guid=" + guid + "' style='cursor: pointer;'  />");
}