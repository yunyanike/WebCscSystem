<template>
  <div class="app-container">
    <div class="tip">
      请上传要进行识别的图片文件
    </div>
    <el-upload
      class="upload-demo"
      drag
      action=""
      :limit="1"
      :http-request="uploadImg"
      accept=".jpg,.jpeg,.png,.bmp"
      style="text-align: center; padding-top:10px;padding-bottom:10px;"
    >
      <i class="el-icon-upload" />
      <div class="el-upload__text">将文件拖到此处，或<em>点击上传</em></div>
    </el-upload>
    <el-row style="text-align: center; padding-top:10px;padding-bottom:30px;">
      <el-button type="success" round @click="imageCorrect()">人脸识别</el-button>
      <el-button type="primary" round @click="saveinfoResult()">保存识别后结果</el-button>
      <el-button type="primary" round @click="saveimgResult()">保存识别后图片</el-button>
    </el-row>
    <div v-show="visible" class="tip">
      人脸信息：
    </div>
    <el-input v-show="visible" v-model="confResult" type="textarea" :rows="2" />
    <div v-show="visible" class="tip">
      人脸图片：
    </div>
    <div class="tip">
      <el-image v-show="visible" :src="imgResult" />
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import { saveAs } from 'file-saver'
export default {
  data() {
    return {
      fileData: '',
      confResult: '',
      imgResult: '',
      visible: false
    }
  },
  beforeCreate() {
    // 读取文件
    FileReader.prototype.reading = function({ encode } = 'pms') {
      const bytes = new Uint8Array(this.result) // 无符号整型数组
      const text = new TextDecoder(encode || 'UTF-8').decode(bytes)
      return text
    }
    /* 重写readAsBinaryString函数 */
    FileReader.prototype.readAsBinaryString = function(f) {
      // 如果this未重写onload函数，则创建一个公共处理方式
      if (!this.onload) {
        this.onload = e => { // 在this.onload函数中，完成公共处理
          const rs = this.reading()
          console.log(rs)
        }
      }
      this.readAsArrayBuffer(f) // 内部会回调this.onload方法
    }
  },
  methods: {
    // 储存选择的file文件
    uploadImg(file) {
      this.fileData = file.file
      console.log(file.file)
      this.$message({
        showClose: true,
        message: '图片上传成功！',
        type: 'success'
      })
    },
    // 保存纠错结果
    saveinfoResult() {
      // console.log(this.fileList)
      var tempData = this.confResult
      if (tempData === '') {
        this.$message({
          showClose: true,
          message: '识别结果内容为空！',
          type: 'warning'
        })
      } else {
        var tempResult = new Blob([tempData], { type: 'text/plain;charset=utf-8' })
        saveAs(tempResult, '识别信息结果.txt')
      }
    },
    // 保存纠错结果
    saveimgResult() {
      // console.log(this.fileList)
      var tempData = this.imgResult
      var filename = this.filename
      console.log(filename)
      if (tempData === '') {
        this.$message({
          showClose: true,
          message: '没有误别图片！',
          type: 'warning'
        })
      } else {
        // var tempResult = new Blob([tempData], { type: 'text/plain;charset=utf-8' })
        // saveAs(tempResult, '识别后图片结果.jpeg')
        const imgLink = document.createElement('a')
        imgLink.href = tempData;
        // a.download = "文件分享二维码"; //文件名
        imgLink.setAttribute("download", filename + ".png");//调用download属性，并添加名字
		    document.body.appendChild(imgLink);
		    imgLink.click(); // 触发点击
		    document.body.removeChild(imgLink); // 然后移除
      }
    },
    imageCorrect() {
      var that = this
      if (that.fileData === '') {
        this.$message({
          showClose: true,
          message: '请先选择要进行识别图片文件！',
          type: 'warning'
        })
        that.confResult = ''
        that.imgResult = ''
        that.visible = false
        return
      }
      var config = {
        headers: {
          'Content-Type': 'multipart/form-data'
        }
      }
      var form = new FormData()
      form.append('file', that.fileData)
      // 请求后端API服务，请求方法为post
      axios.post('http://127.0.0.1:8000/v1/faceDetect/', form, config).then((response) => {
        // console.log(response.data.infoResults)
        that.confResult = JSON.stringify(response.data.infoResults)
        that.imgResult = `data:image/png;base64, ${response.data.imgResult}`
        that.filename = response.data.filename
        that.visible = true
        that.$message({
          showClose: true,
          message: '图片识别完成！',
          type: 'success'
        })
      }).catch((error) => {
        console.log(error)
        that.confResult = ''
        that.visible = false
        that.$message({
          showClose: true,
          message: '请求出现异常！',
          type: 'error'
        })
      })
    }
  }
}

</script>

<style scoped>
  .tip {
    font-family: 宋体;
  font-size: 18px;
	font-weight: bold;
	margin-bottom: 20px;
  margin-bottom: 10px;
  text-align: center;
  }
</style>
