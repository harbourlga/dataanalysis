function createGuid() {
      return (((1 + Math.random()) * 0x10000) | 0).toString(16).substring(1);
}
function ref() {
     var guid = createGuid() + createGuid() + "-" + createGuid() + "-" + createGuid() + createGuid() + "-" + createGuid() + createGuid() + createGuid(); //CreateGuid();
     $("#txthidGuid").val(guid);
     $("#divYzmImg").html("<img alt='���ˢ����֤�룡' name='validateCode' id='ImgYzm' onclick='ref()'  title='����л���֤��' src='/ValiCode/CreateCode/?guid=" + guid + "' style='cursor: pointer;'  />");
}