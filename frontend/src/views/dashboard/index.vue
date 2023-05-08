<template>
    <div>
    
        <div class="wrap">
    
            <!-- <p>单个vue文件</p> -->
        
            <div class="content">
                <el-image :src="url"/>
                <h1>若森·画江湖</h1>
                <h2>玄机·天行九歌</h2>
    
            </div>
    
        </div>
    
        <div>
    
            <p class="align-center">单行文字垂直居中 height = line-height;水平居中text-align: center; </p>
    
        </div>
    
    
    
    </div>
</template>

<script>
import { mapGetters } from 'vuex'
export default {
  name: 'Dashboard',
  data() {
    return {
      url: require('/src/assets/img/paddle.jpeg')
    }
  },
  computed: {
    ...mapGetters([
      'name'
    ])
  }
}
</script>

<style scoped>
/* display: table 表格  display: table-cell; 单元格*/

/* vertical-align: middle;垂直居中（只对行内元素有效）  text-align: center; 水平居中（只对行内元素有效）*/

.wrap {
    height: 10.666667rem;
    width: 100%;
    border: 1px blue solid;
    display: table;
    text-align: center;
}

.content {
    vertical-align: middle;
    display: table-cell;
}

img {
    width: 5.333333rem;
    height: 2.666667rem;
}

.align-center {
    width: 100%;
    height: 4rem;
    line-height: 4rem;
    text-align: center;
}
</style>