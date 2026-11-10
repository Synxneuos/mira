package net.synxneuos.mira.ui.ball

/** The look's name in the interface language. Lives here because the look's own data is shared with the desktop. */
fun net.synxneuos.mira.ui.ball.BallLook.label(ctx: android.content.Context): String = when (name) {
    "mira", "mira" -> net.synxneuos.mira.i18n.AppLocale.str(ctx, net.synxneuos.mira.R.string.ball_look_mira)
    "cream" -> net.synxneuos.mira.i18n.AppLocale.str(ctx, net.synxneuos.mira.R.string.ball_look_cream)
    "bajie" -> net.synxneuos.mira.i18n.AppLocale.str(ctx, net.synxneuos.mira.R.string.ball_look_bajie)
    "rabbit" -> net.synxneuos.mira.i18n.AppLocale.str(ctx, net.synxneuos.mira.R.string.ball_look_rabbit)
    "bear" -> net.synxneuos.mira.i18n.AppLocale.str(ctx, net.synxneuos.mira.R.string.ball_look_bear)
    "imp" -> net.synxneuos.mira.i18n.AppLocale.str(ctx, net.synxneuos.mira.R.string.ball_look_imp)
    else -> name
}
