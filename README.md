<h2>CASO DE CHURN DO FAST BANK</h2>
<h3>PROBLEMA DE NEG&Oacute;CIO</h3>
<p>O Fast Bank &eacute; uma grande empresa de servi&ccedil;os banc&aacute;rios que atua principalmente na Europa, oferecendo uma variedade de produtos financeiros, desde contas banc&aacute;rias at&eacute; investimentos e seguros. Recentemente, a equipe de Analytics percebeu um aumento na taxa de cancelamento de contas, atingindo n&uacute;meros sem precedentes para a empresa. Preocupado com essa tend&ecirc;ncia, o time planejou uma a&ccedil;&atilde;o para reduzir a evas&atilde;o de clientes.</p>
<p>Para enfrentar essa queda, a equipe de Analytics da Fast Bank contratou voc&ecirc; como consultor de Data Science com o objetivo de criar um plano de a&ccedil;&atilde;o para reduzir a evas&atilde;o de clientes, ou seja, impedir que os clientes cancelem seus contratos e n&atilde;o renovem por mais 12 meses. Ao final da consultoria, voc&ecirc; precisa entregar ao CEO da Fast Bank um modelo em produ&ccedil;&atilde;o que receber&aacute; uma base de clientes em churn via API e desenvolver&aacute; uma poss&iacute;vel a&ccedil;&atilde;o para evitar que o cliente entre em churn, como oferecer um cupom de desconto ou algum outro incentivo financeiro para renovar o contrato por mais 12 meses.</p>
<p>Churn &eacute; uma m&eacute;trica que indica o n&uacute;mero de clientes que cancelaram o contrato ou pararam de comprar um produto em um determinado per&iacute;odo de tempo. Por exemplo, clientes que cancelaram o contrato de servi&ccedil;o ou n&atilde;o renovaram ap&oacute;s o vencimento s&atilde;o considerados clientes em churn.</p>
<h3>ESTRUTURA DA SOLU&Ccedil;&Atilde;O</h3>
<p>A metodologia empregada para a cria&ccedil;&atilde;o deste projeto ser&aacute; a CRISP-DM (Cross Industry Standard Process for Data Mining). Essa metodologia consiste em um processo c&iacute;clico de desenvolvimento, com foco na entrega r&aacute;pida de solu&ccedil;&otilde;es e na possibilidade de melhorias e atualiza&ccedil;&otilde;es em cada itera&ccedil;&atilde;o.</p>
<h3>COLETA DE DADOS</h3>
<p>Os dados utilizados neste projeto foram fornecidos na plataforma Kaggle e podem ser acessados atrav&eacute;s deste link: <a href="https://www.kaggle.com/datasets/mervetorkan/churndataset">ChurnDataset</a>.</p>
<h3>EXPLORA&Ccedil;&Atilde;O DE DADOS</h3>
<p>O conjunto de dados possui dez mil linhas e quatorze colunas, sendo 11 num&eacute;ricas e 3 categ&oacute;ricas. N&atilde;o h&aacute; c&eacute;lulas vazias nem duplicadas. Destaca-se que a propor&ccedil;&atilde;o da vari&aacute;vel alvo est&aacute; desbalanceada, com 3,91 clientes n&atilde;o churn para cada cliente em churn.</p>
<p><img src="https://github.com/gabrielpastega/churn_prediction/blob/main/img/proporcao_clientes.png" alt="" /></p>
<p>Observa-se que, em sua maioria, os clientes em churn e os n&atilde;o churn possuem distribui&ccedil;&otilde;es e padr&otilde;es similares. No entanto, existem diferen&ccedil;as significativas nas vari&aacute;veis de idade, produto, cart&atilde;o de cr&eacute;dito e g&ecirc;nero.</p>
<p>Quando analisamos os valores de churn dos clientes por idade, observamos um maior n&uacute;mero de clientes em churn na faixa et&aacute;ria entre 40 e 50 anos, em compara&ccedil;&atilde;o com os clientes n&atilde;o churn, que est&atilde;o mais concentrados entre 30 e 40 anos.</p>
<p><img src="https://github.com/gabrielpastega/churn_prediction/blob/main/img/churn_por_idade.png" alt="" /></p>
<p>H&aacute; uma maior evas&atilde;o entre os clientes que adquirem 3 produtos e uma evas&atilde;o total entre os clientes que adquiriram 4 produtos oferecidos pelo Fast Bank.</p>
<p><img src="https://github.com/gabrielpastega/churn_prediction/blob/main/img/churn_por_produto.png" alt="" /></p>
<p>Em rela&ccedil;&atilde;o &agrave; posse de cart&atilde;o de cr&eacute;dito, os clientes que possuem cart&atilde;o apresentam uma maior taxa de evas&atilde;o.</p>
<p><img src="https://github.com/gabrielpastega/churn_prediction/blob/main/img/churn_por_cart%C3%A3o_de_cr%C3%A9dito.png" alt="" /></p>
<h3>MODELAGEM DE DADOS</h3>
<p>Neste projeto, optou-se pelo uso do TargetEncoder para a parte de codifica&ccedil;&atilde;o, RobustScaler para redimensionamento e o algoritmo selecionado foi o CatBoost Classifier,&nbsp;conhecido por sua efici&ecirc;ncia e escalabilidade. Em seguida, o algoritmo foi aprimorado utilizando a ferramenta Optuna para otimizar seus hiperpar&acirc;metros. O resultado obtido foi o seguinte:</p>
<p><img src="https://github.com/gabrielpastega/churn_prediction/blob/main/img/metricas_catboostclassifier.png" alt="" /></p>
<h3>AN&Aacute;LISE DOS RESULTADOS</h3>
<p>Ap&oacute;s a implementa&ccedil;&atilde;o e testes do modelo, identificamos os clientes em churn e os categorizamos em tr&ecirc;s categorias com base em sua contribui&ccedil;&atilde;o financeira para o Fast Bank.</p>
<p>De acordo com a equipe de Analytics do Fast Bank, cada cliente que possui uma conta banc&aacute;ria gera um valor monet&aacute;rio correspondente a 15% do valor estimado de seu sal&aacute;rio, se for inferior &agrave; m&eacute;dia salarial, e 20% se for superior &agrave; m&eacute;dia salarial, durante o per&iacute;odo de vig&ecirc;ncia da conta. Esse valor &eacute; calculado anualmente.</p>
<p>Ap&oacute;s a categoriza&ccedil;&atilde;o, implementamos um algoritmo de sele&ccedil;&atilde;o de clientes com base no or&ccedil;amento previsto de R$10.000,00, no qual enviaremos incentivos financeiros aos clientes, com o objetivo de selecionar aqueles que, se renovarem seus contratos, maximizem o rendimento total do Fast Bank. Utilizamos a t&eacute;cnica de programa&ccedil;&atilde;o din&acirc;mica para calcular essa solu&ccedil;&atilde;o.</p>
<p>Com essa sele&ccedil;&atilde;o, conseguimos atingir 130 clientes em churn, potencialmente recuperando cerca de R$3.297.195,00 que seriam perdidos caso esses contratos n&atilde;o fossem renovados.</p>
<h3>MODELO EM PRODU&Ccedil;&Atilde;O</h3>
<p>Ap&oacute;s verificar os resultados e o desempenho do algoritmo gerado nesta primeira vers&atilde;o, decidimos implementar a solu&ccedil;&atilde;o. Como esta &eacute; a primeira vers&atilde;o, &eacute; importante destacar a import&acirc;ncia de validar sua precis&atilde;o, usabilidade e obter feedback para corre&ccedil;&otilde;es e melhorias.</p>
<p>A solu&ccedil;&atilde;o criada pode ser acessada atrav&eacute;s da ferramenta Google Sheets, que faz uma requisi&ccedil;&atilde;o ao modelo instanciado por meio de um script e retorna a lista de clientes selecionados para receber o incentivo financeiro.</p>
<p><img src="https://github.com/gabrielpastega/churn_prediction/blob/main/img/google_sheets.gif" alt="" /></p>
<p>Esse processo utiliza uma plataforma em nuvem chamada Render, que hospeda nosso algoritmo e aplicativo gratuitamente.</p>
<p>Caso precise de mais informa&ccedil;&otilde;es ou tenha d&uacute;vidas, estou &agrave; disposi&ccedil;&atilde;o para disponibilizar todos os documentos utilizados neste projeto.</p>
<h2>PŔOXIMOS PASSOS</h2>
<ul>
<li>Feature Engineering das vari&aacute;veis</li>
<li>Melhoria do desempenho do modelo</li>
<li>Verificar feedback do modelo e ajustar conforme necess&aacute;rio</li>
</ul>
