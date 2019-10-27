import Vue from 'vue'
import Router from 'vue-router'
import smartHackathon from '@/components/smartHackathon'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'smartHackathon',
      component: smartHackathon
    }
  ]
})
