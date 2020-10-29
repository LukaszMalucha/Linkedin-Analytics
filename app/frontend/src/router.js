import Vue from "vue";
import Router from "vue-router";
import Home from "./views/Home.vue";
import Finance from "./views/Finance.vue";
import Companies from "./views/Companies.vue";
import NotFound from "./views/NotFound.vue";

Vue.use(Router);

export default new Router({
  mode: "history",
  routes: [
    {
      path: "/",
      name: "home",
      component: Home
    },
    {
      path: "/finance",
      name: "finance",
      component: Finance
    },
    {
      path: "/companies/:category",
      name: "companies",
      component: Companies,
      props: true
    },
    {
      path: "*",
      name: "page-not-found",
      component: NotFound,
    },
  ]
});
