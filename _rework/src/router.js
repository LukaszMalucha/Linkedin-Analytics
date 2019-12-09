import Vue from "vue";
import Router from "vue-router";
import Home from "./views/Home.vue";
import NotFound from "./views/NotFound.vue";
import Finance from "./views/Finance.vue";
import IT from "./views/IT.vue";
import Education from "./views/Education.vue";

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
      path: "/it",
      name: "it",
      component: IT
    },
    {
      path: "/finance",
      name: "finance",
      component: Finance

    },
    {
      path: "/education",
      name: "education",
      component: Education

    },
    {
      path: "*",
      name: "page-not-found",
      component: NotFound,
    }

  ]
});
