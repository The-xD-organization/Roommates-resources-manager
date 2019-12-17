<template>
    <default-layout>
        <body class="about-page">
            <div>
                <div>
                    <div class="sec1">
                        <b-jumbotron header="RoomMates Manager"
                        class="my-2 text-center jumbotron1"
                        header-level="4"
                        text-variant="dark"
                        lead="Aplikacja do zarządzania zasobami dla współlokatorów">
                        </b-jumbotron>
                            <b-button class="btn1"
                            variant="primary" href="#section2">V</b-button>
                    </div>
                    <div id="section2" class="sec2">
                        <div class="about-app">
                        <h2 class="mt-2 font-weight-light">Funkcjonalności</h2>
                        </div>
                        <b-container fluid>
                            <b-row class="m-3 justify-content-sm-center">
                                <b-col cols="12" sm="5" md="4" class="m-2">
                                    <b-card
                                    title="Dashboard"
                                    sub-title="(work in progress)">
                                    <div>
                                    <b-img
                                    src="https://image.flaticon.com/icons/png/512/1508/1508776.png"
                                    class="utility_img" alt="Responsive image"></b-img>
                                    </div>
                                    <p>Na ekranie głównym wyświetlane będą nowe rachunki,
                                        oczekujące obowiązki oraz skróty do funkcjonalności.</p>
                                    </b-card>
                                </b-col>
                                <b-col cols="12" sm="5" md="4" class="m-2">
                                    <b-card
                                    title="Rachunki">
                                     <div>
                                    <b-img
                                    src="https://image.flaticon.com/icons/png/512/313/313434.png"
                                    class="utility_img" alt="Responsive image"></b-img>
                                    </div>
                                    <p> Opcja ta pozwoli w prosty sposób
                                        wprowadzać, przechowywać oraz zarządzać rachunkami.
                                        Rachunki będą posiadały odpowiednie kategorie,
                                        która w przyszłości pozwoli na ich filtrowanie.
                                    </p>
                                    </b-card>
                                </b-col>
                                <b-col cols="12" sm="5" md="4" class="m-2">
                                    <b-card
                                    title="Obowiązki"
                                    sub-title="(work in progress)">
                                     <div>
                                    <b-img
                                    src="https://image.flaticon.com/icons/png/512/839/839860.png"
                                    class="utility_img" alt="Responsive image"></b-img>
                                    </div>
                                    <p>Współlokatorzy będą mogli w prosty sposób dzielić się
                                        obowiązkami.
                                    </p>
                                    </b-card>
                                </b-col>
                                <b-col cols="12" sm="5" md="4" class="m-2">
                                    <b-card
                                    title="Długi"
                                    sub-title="(work in progress)">
                                     <div>
                                    <b-img
                                    src="https://image.flaticon.com/icons/png/512/1547/1547315.png"
                                    class="utility_img" alt="Responsive image"></b-img>
                                    </div>
                                    <p>Funkcjonalność "Długi" ułatwi rozliczanie się między
                                        współlokatorami.</p>
                                    </b-card>
                                </b-col>
                                <b-col cols="12" sm="5" md="4" class="m-2">
                                    <b-card
                                    title="Kalkulator zużycia"
                                    sub-title="(work in progress)"  >
                                     <div>
                                    <b-img
                                    src="https://image.flaticon.com/icons/png/512/710/710088.png"
                                    class="utility_img" alt="Responsive image"></b-img>
                                    </div>
                                    <p>Kalkulator zużycia pozwoli obliczyć cenę za media na
                                        podstawie zużycia odczytanego z liczników.
                                    </p>
                                    </b-card>
                                </b-col>
                            </b-row>
                        </b-container>
                    </div>
                </div>
            </div>
        </body>
    </default-layout>
</template>

<script>
import DefaultLayout from '@/components/layouts/DefaultLayout.vue';


export default {
    name: 'home',
    components: {
        DefaultLayout,
    },
    data() {
        return {
        };
    },

    methods: {
    },
    mounted() {
    },
};
</script>
<style scoped>
.about-page{
    background: transparent;
}
.jumbotron1{
    background: transparent;
        color: white;
}
.jumbotron2{
    background: #17a2b8;
        color: white;
}
.btn1{
    position: static;
    border-radius: 30px;
    background-color: transparent;
    border: none;
    visibility: hidden;
}
.sec1{
    text-align: center;
    position: relative;
    overflow: hidden;
    background: white;
}
.sec2{
    max-height: fit-content;
    position: relative;
    overflow: hidden;
    text-align: center;
    margin-bottom: 10px;
}
.sec3{
    position: relative;
    overflow: hidden;
    text-align: center;
    margin-bottom: 10px;
}
.utility_img{
    max-height: 128px;
    max-width: 128px;
}
.about-app{
}
</style>
