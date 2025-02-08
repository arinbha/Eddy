import { z } from "zod";

import {
    createTRPCRouter,
    protectedProcedure,
    publicProcedure,
} from "~/server/api/trpc";

export const loginRouter = createTRPCRouter({
    login: publicProcedure
        .input(z.object({ username: z.string().min(1) }))
        .query(async ({ ctx , input }) => {
            const res = await ctx.client.post('/login', {
                username: input.username,
                password: "",
            });

            const schema = z.object({
                id: z.number(),
                username: z.string(),
                preferences: z.any()
            })

            const result = await schema.safeParseAsync(res.data);
            if (result.success)
                return result.data;
        }),


    new_user: publicProcedure
        .input(z.object({ username: z.string().min(1) }))
        .query(async ({ ctx , input }) => {
            const res = await ctx.client.post('/new_user', {
                username: input.username,
                password: "",
            });

            const schema = z.object({
                id: z.number(),
                username: z.string(),
                preferences: z.any()
            })

            const result = await schema.safeParseAsync(res.data);
            if (result.success)
                return result.data;
        }),
});
