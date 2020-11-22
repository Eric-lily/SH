import CryptoJs from 'crypto-js'//引用AES源码js
export default {
  // 加密,调用该方法时，传入的data必须是字符串类型，
  //   故，如果要加密对象等类型，需要先用JSON.stringify()将其字符串化再传入
  encryptByAES (data) {
    let keyStr = 'TheKeyOfmyDatadx' // 16位，密钥字符串
    let key = CryptoJs.enc.Utf8.parse(keyStr) // 将字符串的转为WordArray类型
    let mydata = CryptoJs.enc.Utf8.parse(data)
    // console.log('key:', key, 'mydata:', mydata)
    let udata = CryptoJs.AES.encrypt(mydata, key, {
      mode: CryptoJs.mode.ECB, // 加密模式，ECB模式
      padding: CryptoJs.pad.Pkcs7 // 填充方式
    })
    let encrypted = udata.toString()//  返回的是base64的密文,是字符串类型
    return encrypted
  },
  // 解密, 调用该方法时，传入的data是base64的密文
  decryptByAES (data) {
    let keyStr = 'TheKeyOfmyDatadx'
    let key = CryptoJs.enc.Utf8.parse(keyStr)
    let udata = CryptoJs.AES.decrypt(data, key, {
      mode: CryptoJs.mode.ECB,
      padding: CryptoJs.pad.Pkcs7
    })
    let decrypted = udata.toString(CryptoJs.enc.Utf8)// 返回的是加密之前的原始数据,是字符串类型
    return decrypted
  }
}