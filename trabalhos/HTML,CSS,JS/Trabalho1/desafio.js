function verifica(){
    let nomes = ["Pedro", "Lucas", "Ana"];
    let senhas =["123", "1234", "12345"];

    const mensagem = document.getElementById("msg");
    const test = document.getElementById("texto");
    const name = document.getElementById("username").value;
    const acesso = document.getElementById("senha").value;

    let correto = false;

    for(let i = 0; i < nomes.length; i++){
        if(name === nomes[i] && acesso === senhas[i]){
            correto = true;
            break;
        }
    }
    if(correto){
        mensagem.innerHTML = "Login Realizado com Sucesso!";
    } else{
        mensagem.innerHTML = "Digitação errada. Verificar Login e Senha!";
    }
}