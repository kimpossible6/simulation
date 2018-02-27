


clear
model = arima('Constant',5,'MA',{2/3,1/3},...
              'MALags',[1,2],'Variance',9);
rng('default')
Y = simulate(model,10000,'NumPaths',400);
% figure
% plot(var(Y,0,2),'Color',[.75,.75,.75],'LineWidth',1.5)
% xlim([0,60])
% title('Unconditional Variance')
% hold on
% plot(1:60,.336*ones(60,1),'k--','LineWidth',2)
% legend('Simulation','Theoretical',...
%        'Location','SouthEast')
% hold off

n=10000
a = mean(Y)
mu = sum(mean(Y))/400
sdV = std(Y)
t= tinv(0.95,n-1)
lowerCI = a - t*sdV/sqrt(n)
upperCI = a + t*sdV/sqrt(n)
count1=0
for i=1:length(a)
%     value = a(i)
    if(5 >= lowerCI(i))&&(5 <= upperCI(i))
        count1=count1+1
    end
end
zs=norminv(0.95)
zlowerCI= a-zs*6/sqrt(n)
zupperCI= a+zs*6/sqrt(n)
count2=0
for i=1:length(a)
    if(5 >= zlowerCI(i)) && (5 <= zupperCI(i))
        count2=count2+1
    end
end

count1=count1
count2=count2
        