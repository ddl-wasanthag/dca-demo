library(ggplot2)
plot <- ggplot(df2) +
 aes(x = Species, y = Flipper.Length..mm., colour = Sex, size = Culmen.Length..mm.) +
 geom_col(fill = "#112446") +
 scale_color_hue(direction = 1) +
 labs(title = "DCA Demo") +
 theme_classic() +
 theme(legend.position = "none")
plot

