<template>
<div id="bg">
  <div class="container">
    <h1> <b>Accidents Panel</b> </h1>
      <div class="content">
        <div class="tabs" v-for="(x, index) in msg.slice().reverse()" v-bind:key="(x, index)"> 
          
          <el-collapse v-model="activeNames">
            <el-collapse-item>
              <template slot="title">
                Incident on {{ x.time }}
              </template>

              <div>Latitude, longitude: ({{ x.x_coordinate }}, {{ x.y_coordinate }})</div>
              <div>Abnormal driving pattern : {{ x.is_squiggly }}</div>
              <div>Crash : {{ x.airbag_open }}</div>

            </el-collapse-item>
          </el-collapse>
        </div>
        
      </div>
  </div>
</div>
</template>

<script>
import jsondata from '../../../../car.json'
export default {
  data () {
    return {
      msg: jsondata.cars
    }
  },
  method: {
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
#bg {
  z-index: -9999;
  top: 0;
  background-color: #67C23A;
  width: 100%;
  height: 100%;
  position: absolute;
}
#notif {
  color: #F56C6C;
  margin-right: 5px;
}
.container {
  border-radius: 15px;
  background-color: #F2F6FC;
  height: 650px;
  width: 750px;
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  box-shadow: 0px 0px 25px 0px rgba(82, 99, 175, 0.274);
}

.content {
  border-radius: 15px;
  background-color: white;
  height: 535px;
  width: 680px;
  position: absolute;
  top: 54%;
  left: 50%;
  transform: translate(-50%, -50%);
  overflow: scroll;
}

.tabs {
  padding: 10px;
  box-shadow: 0 0 2px 0 rgba(144,147,153,0.5);
  margin: 15px;
}
a {
  color: #42b983;
}
</style>
