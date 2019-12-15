<template>
    <login-layout>
        <body class="login-page">
            <div class="page-header clear-filter">
            <b-navbar  class="navbar-transparent" type="dark" toggleable="lg">
                <b-navbar-brand>
                    <router-link
                        class="navbar-brand pl-5"
                        to="/login">
                            RoomMates Manager
                        </router-link>
                </b-navbar-brand>
            </b-navbar>
            <div class="content">
            <div class="container">
                <div class="col-lg-5 ml-auto mr-auto">
                        <b-card class="login">
                        <div>
                            <div class="logo-container">
                                <b-img class="image" alt="Logo"
                                 src="https://image.flaticon.com/user_icons/18063/18063151/1576325119849.svg">
                                </b-img>
                            </div>
                        </div>
                    <h3>Wylogowaliśmy Cię</h3>
                    <p>Przeniesiemy Cię do strony głównej za {{ sec }}...</p>
                    <router-link to="/">
                            Wróć do strony głownej
                    </router-link>
                 </b-card>
                        </div>
                        </div>
                    </div>
                    <footer class="footer">
                    <b-container>
                        <b-row class="text-center">
                            <b-col>
                                <span >Copyright © The-xD-organization</span>
                            </b-col>
                        </b-row>
                    </b-container>
                    </footer>
                </div>
        </body>
    </login-layout>
</template>

<script>
import LoginLayout from '@/components/layouts/LoginLayout.vue';

export default {
    name: 'logout',
    components: {
        LoginLayout,
    },
    data() {
        return {
            sec: 5,
        };
    },
    methods: {
        countdown() {
            const timer = setInterval(() => {
                this.sec = this.sec - 1;
                if (this.sec === 0) {
                    clearInterval(timer);
                    this.$router.replace('/');
                }
            }, 1000);
        },
    },
    mounted() {
        this.$store.dispatch('logout');
        this.countdown();
    },
};
</script>
<style scoped>
.navbar-transparent{
    background-color: transparent!important;
    box-shadow: none;
    color: #ffffff;
    padding-top:20px;
}
.content{
    margin-top: 8%;
}
.container{
    height: 100%;
    text-align: center;
    position: relative;
}
.clear-filter{
    background: linear-gradient(0deg,#ccffcc,#17a2b8)
}
.login{
    border:0;
    display: inline-block;
    position: relative;
    width: 100%;
    margin-bottom: 30px;
    padding-bottom: .7rem;
    max-width: 400px;
    background: transparent;
    box-shadow: none;
}
.input-style{
    margin-bottom: 40px;
    position: relative;
    align-items: stretch;
    width: 100%;
    background-color: #ffffff54;
    border:0;
    border-radius: 30px;
}
.btn-submit{
    border:0;
    width: 95%;
    border-radius: 30px;
    background-color: #17a2b8;
    padding: 10px 48px;
    margin: 5px 1px;
}
.page-header{
    min-height: 100vh;
    max-height: 999px;
    position: relative;
    overflow: hidden;
}
.footer{
    position: absolute;;
    bottom: 0;
    width: 100%;
    height: 40px;
}
.logo-container{
    margin-bottom: 35px;
    background: transparent;
}
.image{
    max-height: 128px;
    position: relative;
}
</style>
